# data_preparation.py
# Creates working dataframe with merged data from all sources including engineered features.

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def create_working_df():
    # Get records for teams, need year n-1 to predict n
    records_df = pd.read_csv('../data/records_by_year_calcs.csv')

    # Sort by team and year
    records_df = records_df.sort_values(by=['team', 'year'])

    # Shift recent_win_pct by +1 years
    records_df['recent_win_pct'] = records_df.groupby('team')['recent_win_pct'].shift(1)
    records_df['prev_win_pct'] = records_df.groupby('team')['win_pct'].shift(1)
    # Keep only records from 2014
    records_2014_df = records_df[records_df['year'] >= 2014].copy()

    # Get recruiting info. Need year n to predict year n
    recruiting_df = pd.read_csv('../data/team_recruiting_w_blue_chip_ratios.csv')
    # Filter the years we need
    recruiting_2014_df = recruiting_df[recruiting_df.year >= 2014].copy()
    # Remove/rename some columns
    recruiting_2014_df = recruiting_2014_df.drop(columns=['total', 'blue_sums', 'total_sums'])
    recruiting_2014_df = recruiting_2014_df.rename(columns={'rank': 'recruiting_rank', 'points': 'recruiting_rating'})

    # Returning talent. Need year n to predict year n
    returning_2014_df = pd.read_csv('../data/returning_players_2014.csv')
    returning_2014_df = returning_2014_df.drop(columns=['conference'])

    # ELO/FPI Ratings. Need year n-1 to predict year n
    ratings_df = pd.read_csv('../data/team_conference_ratings.csv')
    # Grab data going back to 2013, 1 year before starting analysis
    ratings_2014_df = ratings_df[ratings_df.year >= 2013].copy()
    # Relabel years by +1 so they are rating at start of new season
    ratings_2014_df['year'] = ratings_2014_df['year'] + 1

    # Last Season Traditional Stats. Need year n-1 to predict year n
    trad_stats_df = pd.read_csv('../data/season_stats_w_totals.csv')[['year', 'team', 'totalYards', 'turnover_margin', 'total_tds', 'games']]
    # Switch year by 1 so we're using last season's stats
    trad_stats_df['year'] = trad_stats_df['year'] + 1
    # Fix NaN values
    trad_stats_df = trad_stats_df.fillna(0)
    # Keep from 2014 on (AFTER relabel)
    trad_stats_df = trad_stats_df[trad_stats_df['year'] >= 2014]

    # Last Season Advanced Stats. Need year n-1 to predict year n
    adv_stats_df = pd.read_csv('../data/advanced_stats_seasons.csv')
    # Switch names of a few categories and drop uneeded columns
    adv_stats_df = adv_stats_df.rename(columns={'season': 'year'})
    adv_stats_df = adv_stats_df.drop(columns=['offense', 'defense', 'conference'])
    # Switch year by 1 so we're getting last seasons stats
    adv_stats_df['year'] = adv_stats_df['year'] + 1
    # Filter data from 2014 - 2023 (10 years of data)
    adv_stats_2014_df = adv_stats_df[adv_stats_df['year'] >= 2014].copy()

    # Strength of Schedule. Need year n to predict year n for strength of schedule
    sos_df = pd.read_csv('../data/schedule_strength.csv')
    # Shift strength of record column to add 1 year so year n-1 predicts year n
    sos_df['sor'] = sos_df.groupby('team')['sor'].shift(1)

    # Coaching Information. Need coach in year n but career win percentage from year n-1.
    coaches_df = pd.read_csv('../data/coach_career_win_pct.csv')
    coaches_df = coaches_df.rename(columns={'name': 'coach'})
    coaches_df['career_win_pct'] = coaches_df.groupby('coach')['career_win_pct'].shift(1)
    coaches_df['career_win_pct'] = coaches_df['career_win_pct'].fillna(0)
    # Keep only a couple of columns
    coaches_df = coaches_df[['coach', 'team', 'year', 'career_win_pct']].copy()

    # Merge into working df
    df = records_2014_df.merge(ratings_2014_df, on=['year', 'team', 'conference']) \
                            .merge(recruiting_2014_df, on=['year', 'team']) \
                            .merge(returning_2014_df, on=['year', 'team']) \
                            .merge(trad_stats_df, on=['year', 'team']) \
                            .merge(adv_stats_2014_df, on=['year', 'team']) \
                            .merge(coaches_df, on=['year', 'team']) \
                            .merge(sos_df, on=['year', 'team'])
    df.to_csv('/Users/reggiebain/erdos/cfb-modeling-erdos/data/working_df.csv', index=False)
    print('Working dataframe created at /data/working_df.csv!')

def get_working_df():
        create_working_df()
        return pd.read_csv('/Users/reggiebain/erdos/cfb-modeling-erdos/data')
