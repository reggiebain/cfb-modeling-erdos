'''
tiers.py
Returns a working dataframe filtered by the tiers of college teams as defined by 
https://www.cllct.com/sports-collectibles/memorabilia/how-much-did-your-school-get-to-appear-in-ea-college-football-25
'''
import pandas as pd
#from data_preparation import get_working_df

tier_one = ['Alabama', 'Ohio State', 'Clemson', 'Notre Dame', 'Oklahoma',
            'Georgia', 'LSU', 'Michigan', 'Oregon', 'Oklahoma State',
            'Penn State', 'Utah', 'Iowa']
tier_two = ['USC', 'Florida State', 'Texas', 'Wisconsin', 'Florida',
            'Washington', 'Cincinatti', 'Tennessee', 'TCU', 'Ole Miss',
            'Boise State', 'Northwestern', 'Auburn', 'Baylor', 'Michigan State',
            'Stanford', 'Louisville', 'UCF', 'Memphis', 'Kansas State',
            'NC State', 'Miami', 'Mississippi State', 'Louisiana', 'Pittsburgh',
            'Liberty', 'Kentucky', 'Utah State', 'San Diego State', 'Texas A&M',
            'USF', 'South Florida', 'UCLA', 'Arizona', 'West Virginia',
            'Houston', 'Virginia Tech', 'BYU', 'North Carolina', 'Fresno State',
            'Navy', 'Missouri']
tier_three = ['Syracuse', 'Washington State', 'Kansas', 'Marshall', 'South Carolina', 
              'Army', 'Troy', 'Coastal Carolina', 'Arkansas', 'Colorado',
              'Western Michigan', 'Minnesota', 'Indiana', 'Air Force', 'Iowa State',
              'Appalachian State', 'Tulane', 'Ball State', 'Buffalo', 'Arizona State',
              'Wake Forest', 'Oregon State', 'Western Kentucky', 'Georgia Tech',
              'SMU', 'San Diego State']
tier_four = ['Tulsa', 'Central Michigan', 'Kent State', 'Middle Tennessee', 'Texas Tech',
             'Old Dominion', 'Connecticut', 'Georgia Southern', 'Vanderbilt','Georgia State',
             'Colorado State', 'Maryland', 'New Mexico State', 'Duke', 'Arkansas State',
             "Hawai'i", 'UNLV', 'Purdue', 'UTEP', 'Rice', 'California', 'Rutgers',
             'Louisiana Monroe', 'Sam Houston State', 'Wyoming', 'Boston College',
             'Toledo', 'Charlotte', 'Eastern Michigan','Miami (OH)', 'UAB',
             'South Alabama', 'Eastern Washington', 'East Carolina', 'UMass', 'Northern Illinois',
             'Nebraska', 'UT San Antonio', 'Nevada', 'Virginia', 'Bowling Green',
             'Florida Atlantic', 'Temple', 'Florida International', 'New Mexico State',
             'Ohio', 'Jacksonville State', 'Louisiana Tech', 'James Madison', 'Akron',
             'Texas State', 'Southern Mississippi', 'Illinois', 'Kennesaw State']     

def pick_tier(tiers = 'all'):
    """
    Reads a CSV file containing college football data and filters teams based on tiers.

    Parameters:
    - tiers (str or list, optional): Specifies the tiers of teams to filter. Default is 'all'.
        - If 'all', returns all teams.
        - If a list of tier numbers, returns teams belonging to those tiers.
        - If an integer representing a single tier, returns teams belonging to that tier.
    
    Returns:
    - DataFrame: Filtered DataFrame containing teams based on the specified tiers.
    """
    df = pd.read_csv('/Users/reggiebain/erdos/cfb-modeling-erdos/data/working_df.csv')
    if tiers == 'all':
        return df
    elif tiers == [1, 2]:
        return df[df['team'].isin(tier_one + tier_two)]    
    elif tiers == 1:
        return df[df['team'].isin(tier_one)]
    elif tiers == 2:
        return df[df['team'].isin(tier_two)] 
    elif tiers == 3:
        return df[df['team'].isin(tier_three)]
    elif tiers == [2,3]:
        return df[df['team'].isin(tier_two + tier_three)]

def get_tier(team):
    """
    Determines the tier of a given team based on predefined tier lists.

    Parameters:
    - team (str): The name of the team whose tier is to be determined.

    Returns:
    - int: The tier of the team.
        - Returns 1 if the team is in tier one.
        - Returns 2 if the team is in tier two.
        - Returns 3 if the team is in tier three.
        - Returns 0 if the team is not found in any tier.

    Usage:
    This function is intended to be used with the `apply` method on a DataFrame column.
    For example:
        test['tier'] = test['team'].apply(get_tier)
    """
    if team in tier_one:
        return 1
    elif team in tier_two:
        return 2
    elif team in tier_three:
        return 3
    else:
        return 0                  