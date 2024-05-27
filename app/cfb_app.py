import pandas as pd
import plotly.express as px
import streamlit as st
import folium
import seaborn as sns
from streamlit_folium import st_folium

team_info_df = pd.read_csv('../data/team_info.csv')
recruiting_df = pd.read_csv('../data/team_recruiting_w_blue_chip_ratios.csv')
working_df = pd.read_csv('../data/working_df.csv')
player_recruiting_df = pd.read_csv('../data/player_recruiting.csv')

# Set possible years and teams
years = range(2014, 2023+1)
teams = team_info_df['team'].unique()

# Set year selectors on sidebar
selected_year = st.sidebar.selectbox('Select Year', years)
selected_team = st.sidebar.selectbox('Select Team', teams)

# Create map with location of school
def draw_map(year, team):
    # Get info for the team
    team_row = team_info_df[team_info_df.team == team]
    st.image(team_row['logo'].values[0], width=100)
    # Get location
    latitude = team_row['latitude']
    longitude = team_row['longitude']
    # Get logo
    #logo = team_row['logo']
    icon = folium.CustomIcon(team_row['logo'].values[0], icon_size=(50, 50))
    # Draw the map
    #st.map(team_row, latitude=latitude,longitude=longitude,size=200)
    map = folium.Map(location=[latitude, longitude], zoom_start=6)
    folium.Marker(location=[latitude, longitude], popup=team).add_to(map)
    st_folium(map)

# Draw the map
draw_map(selected_year, selected_team)

def show_recruits(year, team):
    df = player_recruiting_df[(player_recruiting_df['year']==year) 
                         & (player_recruiting_df['school']==team)]
    df['year'] = df['year'].astype(str)
    st.dataframe(df.set_index('year'))
show_recruits(selected_year, selected_team)

def show_elo(year, team):
    fig = px.line(working_df[working_df['team']==team], 
                x='year', 
                y='elo', 
                #orientation='h', 
                title='ELO Rating Over Time',
                labels={'elo': 'ELO', 'year': 'Year'}
                )
    st.plotly_chart(fig)
    #sns.lineplot(data=working_df[working_df['team']==team], x='year', y='elo')

show_elo(selected_year, selected_team)

    
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
