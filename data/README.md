## Guide to Data
#### draft_invo.csv
- Information about NFL draft picks, potentially for seeing how team talent is affected.
- Names, teams, years, conference, pick number in the draft, round picked in draft, position played

#### nil_data.csv
- NIL valuations and social media followers of the top 100 NIL evaluated college football players
- Only has a handful of actual values for valuations

#### player_recruiting.csv
- Contains all recruits along with the year, their star rating (1-5), numeric rating out of 1, team name, and state they went to high school
- All ratings are from the 247Sports composite rankings system. This will help us calculate the blue-chip ratio and evaluate the overall talent on a team. Data goes back to 2000.

#### returning_players_2014
- Data on "usage" (fraction of players who played snaps returning each year) including passing usage returning (1.0 means their same QB that played all last season returned this season) and rushing usage.
- Data only goes back to 2014 and is team level data.

#### team_conference_ratings_2014
- Teams, years, conferences, and 3 ratings (ELO, FPI, SP+ conference ratings) for each team each year back to 2005.
- <a href="https://en.wikipedia.org/wiki/Football_Power_Index#:~:text=Vegas%20closing%20lines.-,Computation,unit%2C%20derived%20from%20preseason%20expectations.">FPI Explained (Wiki)</a>
- <a href="https://en.wikipedia.org/wiki/Elo_rating_system">ELO Explained (Wiki)</a>
- <a href="https://collegefootballdata.com/sp/trends">SP+ Conference Ratings Explained</a>
- **TODO:** Calculate ELO further back than 2005 at least to 2000.
#### team_info.csv
- Contains list of all "FBS" teams that we're considering and some generic information about each one including logo hyperlinks.
#### team_records_by_year.csv
- List of eavery team and their records (both regular season and bowls/playoffs) for every year since 2000.
- Pre 2006 - Regular Season = 11 games + 1 conference championship (maybe) + 1 bowl game (maybe),
- 2006-2014 - Regular Season = 12 games + 1 conference championship (maybe) + 1 or 2 playoff games (maybe)
#### team_recruiting.csv
- Contains recruiting ratings and rankings (how they compare to others) for each team since 2000.
- Should be a good measure of the overall talent on a roster, especially when combined with blue-chip ratio.
