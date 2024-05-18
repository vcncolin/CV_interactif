import streamlit as st
import pandas as pd
import plotly.express as px

# Load your data
df = pd.read_csv('data.csv')

# Add a title
st.title('Interactive Dashboard for Classes Taught')

# Add a slider in the sidebar
year_range = st.sidebar.slider('Select Year Range', min(df['Année']), max(df['Année']), value=[min(df['Année']), max(df['Année'])])

# Filter data based on selected year range
df_filtered = df[(df['Année'] >= year_range[0]) & (df['Année'] <= year_range[1])]

# Create pie charts
pie_topic = px.pie(df_filtered, values='Volume', names='Sous-groupe', title="Domaine enseigné")
pie_genre = px.pie(df_filtered, values='Volume', names='Niveau', title="Niveau d'études")

# Display pie charts side by side
col1, col2 = st.columns(2)
col1.plotly_chart(pie_topic)
col2.plotly_chart(pie_genre)
