import streamlit as st
import pandas as pd
import plotly.express as px

# Set the sidebar width
#st.set_page_config(layout="wide", initial_sidebar_state="collapsed")

# Load your data
df = pd.read_csv('data.csv')

# Add a title
st.title("Vincent COLIN - Domaines d'enseignement")

# Add a slider in the sidebar
year_range = st.slider('Select Year Range', min(df['Année']), max(df['Année']), value=[min(df['Année']), max(df['Année'])])
field = st.multiselect("Domaine d'enseignement", df['Groupe'].unique(), default=df['Groupe'].unique())

# Filter data based on selected year range
df_filtered = df[(df['Année'] >= year_range[0]) & (df['Année'] <= year_range[1]) & df['Groupe'].isin(field)]

# Create pie charts
pie_topic = px.pie(df_filtered, values='Volume', names='Sous-groupe', title="Matière enseignée", use_container_width = True)
pie_genre = px.pie(df_filtered, values='Volume', names='Niveau', title="Niveau universitaire", use_container_width = True)

# Set the layout of the pie charts
pie_topic.update_layout(margin=dict(l=20, r=20, t=20, b=20))
pie_genre.update_layout(margin=dict(l=20, r=20, t=20, b=20))

# Display pie charts side by side

st.plotly_chart(pie_topic)
st.plotly_chart(pie_genre)

st.dataframe(df_filtered)