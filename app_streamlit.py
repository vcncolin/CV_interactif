import streamlit as st
import pandas as pd
import altair as alt

# Load your data
df = pd.read_csv('data.csv')

# Add a title
st.title('Interactive Dashboard for Classes Taught')

# Add a slider in the sidebar
year_range = st.sidebar.slider('Select Year Range', min(df['Année']), max(df['Année']), value=[min(df['Année']), max(df['Année'])])

# Filter data based on selected year range
df_filtered = df[(df['Année'] >= year_range[0]) & (df['Année'] <= year_range[1])]

# Prepare data for pie charts
topic_data = df_filtered.groupby('Sous-groupe')['Volume'].sum().reset_index().rename(columns={'Sous-groupe': 'category', 'hour volume': 'Volume'})
genre_data = df_filtered.groupby('Niveau')['Volume'].sum().reset_index().rename(columns={'Niveau': 'category', 'hour volume': 'Volume'})

# Create pie charts
base = alt.Chart().encode(
    alt.Theta("Volume:Q").stack(True),
    alt.Color("category:N").legend(None)
)

pie_topic = base.mark_arc(outerRadius=120).transform_filter(alt.FieldEqualPredicate(field='category', one=topic_data['category']))
text_topic = base.mark_text(radius=140, size=20).encode(text="category:N").transform_filter(alt.FieldEqualPredicate(field='category', one=topic_data['category']))

pie_genre = base.mark_arc(outerRadius=120).transform_filter(alt.FieldEqualPredicate(field='category', one=genre_data['category']))
text_genre = base.mark_text(radius=140, size=20).encode(text="category:N").transform_filter(alt.FieldEqualPredicate(field='category', one=genre_data['category']))

# Display pie charts side by side
col1, col2 = st.columns(2)
col1.altair_chart(pie_topic + text_topic)
col2.altair_chart(pie_genre + text_genre)