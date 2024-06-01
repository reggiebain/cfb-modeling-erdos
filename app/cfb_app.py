import pandas as pd
#import plotly.express as px
import streamlit as st
#import folium
import seaborn as sns
import matplotlib.pyplot as plt
#from streamlit_folium import st_folium
import pydeck as pdk
import sys
import path

dir = path.Path(__file__).abspath()
sys.path.append(dir.parent.parent)

# Set config variables
st.set_page_config(page_title = 'CFB Data Explorer', layout='wide')

# Download bunch of data (USE ../data and comment out dir/sys above if running locally)
team_info_df = pd.read_csv('data/team_info.csv')
recruiting_df = pd.read_csv('data/team_recruiting_w_blue_chip_ratios.csv')
working_df = pd.read_csv('data/working_df.csv')
player_df = pd.read_csv('data/player_recruiting.csv')
pred_df = pd.read_csv('data/app_data.csv')
ratings_df = pd.read_csv('data/team_conference_ratings.csv')
trad_stats_df = pd.read_csv('data/season_stats_w_totals.csv')

# Display recent stats
def show_stats(year, team, stat):
    #df = trad_stats_df[(trad_stats_df['year']==year)&(trad_stats_df['team']==team)]
    cols = ['year', 'recent_win_pct', 'talent_level', 'blue_chip_ratio', 
            'total_tds', 'totalYards', 'off_success_rate', 'sos', 'sor', 'career_win_pct']
    df = working_df[(working_df['year']<=year-1) & (working_df['team']==team)][cols]
    #df['year'] = df['year'].astype(str)
    #st.dataframe(df.set_index('year'))
    temp = working_df.copy()
    temp = working_df[(working_df['year']<=year-1) & (working_df['team']==team)]
    conference = temp['conference'].iloc[0]
    plot_df = temp.copy()
    conf_avg_stat = working_df.groupby(by=['year','conference'])[stat].mean().reset_index()
    plot_df = plot_df.merge(conf_avg_stat, on=['year', 'conference'], suffixes=('', '_conf_avg'))
    fig, ax = plt.subplots()
    sns.barplot(data=plot_df[plot_df['team']==team], x='year', y=stat, label = team, ax=ax)
    sns.barplot(data=plot_df, x='year', y=f"{stat}_conf_avg",  label=f"{conference} Average", ax=ax)
    st.pyplot(fig.get_figure())



# Create map with location of school
def draw_map(year, team):
    # Get info for the team
    team_row = team_info_df[team_info_df.team == team]
    #st.image(team_row['logo'].values[0], width=100)
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

def show_recruits(year, team):
    df = player_df[(player_df['year']==year) 
                   & (player_df['school']==team)][['year', 'name', 'star', 
                                                   'state', 'ranking', 'rating', 'position', 'height', 'weight']]
    df['year'] = df['year'].astype(str)
    st.dataframe(df.set_index('year'))

def show_recruit_heatmap(year, team):
    # Get relavent data.
    player_data = player_df[(player_df['year']==year) & (player_df['school']==team)]
    team_data = team_info_df[team_info_df['team']==team]
    
    # Create heatmap layer for map
    heatmap_layer = pdk.Layer(
        'HeatmapLayer',
        data=player_data,
        get_position='[longitude, latitude]',
        opacity=0.8,
        get_weight=1
    )
    
    logo_url = team_info_df[team_info_df.team == team].iloc[0]['logo']
    logo_data = [{"url": logo_url, "width": 2000, "height": 2000, "anchorY": 242}]
    
    marker_layer = pdk.Layer(
        type="IconLayer",
        data=team_data,
        get_position='[longitude, latitude]',
        get_icon = logo_data,
        get_size=4,
        scale_size=15,
        #get_icon=team_info_df[team_info_df.team == team].iloc[0]['logo'],
        #scale_size=150000000000,
        #pickable=True
    )
    map_layers = [heatmap_layer, marker_layer]

    # Default viewing state. Pass values from dataframe here
    view_state = pdk.ViewState(
        latitude=team_data['latitude'].iloc[0],
        longitude=team_data['longitude'].iloc[0],
        zoom=3,
        pitch=0
    )
    # Declare the deck
    deck = pdk.Deck(
        map_style='mapbox://styles/mapbox/light-v9',
        initial_view_state=view_state,
        layers=map_layers
    )
    # Render the Pydeck map in Streamlit
    st.pydeck_chart(deck)    

def show_elo(year, team):
    df = ratings_df[(ratings_df['team']==team) & (ratings_df['year'] <= year)]
    conference = df['conference'].iloc[0]
    plot_df = df.copy()
    conf_avg_elo = ratings_df.groupby(by=['year','conference'])['elo'].mean().reset_index()
    plot_df = plot_df.merge(conf_avg_elo, on=['year', 'conference'], suffixes=('', '_conf_avg'))
    fig, ax = plt.subplots()
    #ax = sns.lineplot(data=plot_df[plot_df['team']==team], x='year', y='elo')
    sns.lineplot(data=plot_df[plot_df['team']==team], x='year', y='elo', label = team, ax=ax)
    sns.lineplot(data=plot_df, x='year', y='elo_conf_avg',  label=f"{conference} Average", ax=ax)
    #plt.tight_layout()
    #st.pyplot(plt.gcf())
    st.pyplot(fig.get_figure())
    return None
    #return fig

#def show_recent_stats(year, team):

def get_current_coach(team):
    row = pred_df[pred_df['team']==team].copy().iloc[0]
    return row['coach']

def show_predicted_records(team):
    df = pred_df[pred_df['team']==team].copy()
    team_row = df.iloc[0]
    st.markdown(f"### Model Predicted 2024 Record: {int(team_row['pred_wins'])}-{int(team_row['pred_losses'])} ($\pm$ 1.908 wins)")

def plot_scatters(team):
    df = working_df
    fig, ax = plt.subplots()
    ax = sns.scatterplot(data=working_df[working_df['team']==team], x='year', y='elo')
    return fig

def main():
    # Set year selectors on sidebar
    st.title("Explore Your Team's Data")
    
    # Split top of page between 2 selectors
    col1, col2 = st.columns(2)

    # Create team selector
    with col1:
        years = range(2014, 2024+1)
        selected_year = st.selectbox('Select Year', years, index=10)
    # Create year selector
    with col2:
        teams = team_info_df['team'].unique()
        selected_team = st.selectbox('Select Team', teams, index=21)

    # Get Team info
    team_row = team_info_df[team_info_df.team == selected_team].iloc[0]
    #st.markdown("# Team Information")

    col1, mid, col2= st.columns([1,1, 25])
    with col1:
        st.image(team_row['logo'], width=60)
    with col2:
        st.markdown(f"## {team_row.team} {team_row.mascot}")

    st.markdown('---')
    show_predicted_records(selected_team)
    st.write('**Note:** Record predicted using model trained on 2014-2023 data. See https://github.com/reggiebain/cfb-modeling-erdos/tree/main for more info!')
    col1, buffer, col2 = st.columns([5, 1, 10])
    with col1:
        st.markdown(f"**Location:** {team_row['city']}, {team_row['state']}")
        st.markdown(f"**Stadium Capacity:** {team_row['stadium_capacity']}")
    with col2:
        st.markdown(f"**Conference:** {team_row['conference']}")
        st.markdown(f"**Current Coach:** {get_current_coach(selected_team)}")    

    left_column, right_column = st.columns(2)
    with left_column:
        #draw_map(selected_year, selected_team)
        st.markdown(f"#### Heatmap of {selected_year} {selected_team} Recruits")
        show_recruit_heatmap(selected_year, selected_team)
        st.markdown(f"#### Information on {selected_year} {selected_team} Recruits")
        show_recruits(selected_year, selected_team)
    with right_column:
        st.markdown(f"#### ELO Rating of {selected_team} Since {selected_year}")
        st.markdown("An ELO rating $R_A$ sets/updates an expectation that a team will win a given game using the formula $E_A = 1/(1+10^{(R_B-R_A)/400})$. ELO ratings were the most important factor in our model for determining wins.")
        #st.pyplot(show_elo(selected_year, selected_team))
        show_elo(selected_year, selected_team)
        ##st.markdown("<br>",unsafe_allow_html=True)
        st.markdown(f"#### Recent Stats for {selected_team} Leading Into {selected_year}")
        #st.markdown(f"#### Plot Different Features vs. Team Win Percentage")
        st.markdown(f"For definitions of these terms see our writeup: https://github.com/reggiebain/cfb-modeling-erdos ")
        features = ['recent_win_pct', 'career_win_pct', 'talent_level', 'blue_chip_ratio', 'off_success_rate', 'sos']
        selected_feature = st.selectbox('Select Feature', features, index=0)
        show_stats(selected_year, selected_team, selected_feature)

    
    # Adding horizontal bar graph
    #st.subheader('Blue Chip Ratio for Each Year')
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

    #draw_blue_chip_plot(selected_year)    
if __name__ == '__main__':
    main()