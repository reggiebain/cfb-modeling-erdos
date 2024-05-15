import pandas as pd
import plotly.express as px
import streamlit as st

team_info_df = pd.read_csv('../data/team_info.csv')
recruiting_df = pd.read_csv('../data/team_recruiting_w_blue_chip_ratios.csv')
recruiting_df

# Set year selector on sidebar
years = recruiting_df['year'].unique()
selected_year = st.sidebar.selectbox('Select Year', years)

# Set up columns
#left_column, right_column = st.columns(2)

# Function to create the map
#def create_map(year):
#    filtered_df = recruiting_df[recruiting_df['year'] == year]
#    state_counts = filtered_df['state'].value_counts().reset_index()
#    state_counts.columns = ['state', 'Recruits']
#    
#    fig = px.choropleth(locations=state_counts['State'], 
#                        locationmode="USA-states", 
#                        color=state_counts['Recruits'],
#                        scope="usa",
#                        color_continuous_scale="Viridis",
#                        title=f"Recruits Distribution for {year}")
#    fig.update_layout(geo=dict(bgcolor= 'rgba(0,0,0,0)', lakecolor='rgba(0,0,0,0)'), margin={"r":0,"t":0,"l":0,"b":0})
#    st.plotly_chart(fig)

#st.title('Recruits Distribution Map')

#create_map(selected_year)

# Adding horizontal bar graph
st.subheader('Blue Chip Ratio for Each Year')
def draw_blue_chip_plot(year):
    blue_chip_data = recruiting_df[(recruiting_df.year == year) & (recruiting_df.blue_chip_ratio > 0)][['team','blue_chip_ratio']].reset_index()
    blue_chip_data_sorted = blue_chip_data.sort_values(by='blue_chip_ratio', ascending=True)

    fig = px.bar(blue_chip_data_sorted, 
                x='blue_chip_ratio', 
                y='team', 
                orientation='h', 
                title='Blue Chip Ratio for Each Year',
                labels={'blue_chip_ratio': 'Blue Chip Ratio', 'Team': 'team'})
    #fig.update_layout(yaxis=dict(rangemode=dict(visible=True), type="linear"))    
    
    st.plotly_chart(fig)

draw_blue_chip_plot(selected_year)    
