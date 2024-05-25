# Jimmys and Joes vs X’s and O’s
### *Predicting results in college sports analyzing talent accumulation and on-field success. A 2024 Erdös Institute Project.*
## Authors 
- Reggie Bain &nbsp;<a href="https://www.linkedin.com/in/reggiebain/"><img src="https://upload.wikimedia.org/wikipedia/commons/c/ca/LinkedIn_logo_initials.png" alt="LinkedIn" style="height: 1em; width:auto;"/></a> &nbsp; <a href="https://github.com/reggiebain"> <img src="https://upload.wikimedia.org/wikipedia/commons/9/91/Octicons-mark-github.svg" alt="GitHub" style="height: 1em; width: auto;"/></a>
- Reid Harris &nbsp;<a href="https://www.linkedin.com/in/reid-harris-71233a1b0/"><img src="https://upload.wikimedia.org/wikipedia/commons/c/ca/LinkedIn_logo_initials.png" alt="LinkedIn" style="height: 1em; width:auto;"/></a> &nbsp; <a href="https://github.com/ReidHarris"> <img src="https://upload.wikimedia.org/wikipedia/commons/9/91/Octicons-mark-github.svg" alt="GitHub" style="height: 1em; width: auto;"/></a>
- Tung Nguyen &nbsp;<a href="https://www.linkedin.com/in/tungprime/"><img src="https://upload.wikimedia.org/wikipedia/commons/c/ca/LinkedIn_logo_initials.png" alt="LinkedIn" style="height: 1em; width:auto;"/></a> &nbsp; <a href="https://github.com/tungprime"> <img src="https://upload.wikimedia.org/wikipedia/commons/9/91/Octicons-mark-github.svg" alt="GitHub" style="height: 1em; width: auto;"/></a> 
## Summary
In this project, we analyze a variety of college football related data in an effort to build a model that can predict on-field success. By considering both talent accumulation and recent on-field results, we aim for a model to predict relevant results for sports betting. In this iteration of the project, **our target is the win percentage of teams in the regular season**.
## Background
Recent legislation has completely changed the landscape of college sports, a multi-billion dollar business with deep roots in American sports culture. With the recent legalization of sports betting in many states and the SCOTUS O’Bannon ruling [1-2] that allows athletes to be paid through so-called “Name-Image-Likeness (NIL)” deals [3], evaluating talent and projecting results in college sports, especially for the purpose of sports betting, is an increasingly interesting problem. We are interested in building a model to project on-field results in college football using a variety of features including an assessment of the talent level of teams as well as recent performance statistics. 
## Dataset(s)
Our dataset comes from a variety of sources including On3 [4], ESPN [5-6], 24/7 Sports [7], The College Football Database [8-9], and SportsReference [10]. We have used APIs and web scraping techniques to identify a wide array of college football features that aim to measure (1) on-field performance and (2) talent level including. These features include wins, conferences, team/player recruiting ratings, points/touchdowns scored, returning players, coaching win percentages, and a host of other more advanced features that we will describe below. <br><br>
As college football has grown exponentially in popularity since 2000 (with TV deals alone providing some universities with over $50 million dollars of annual revenue [11]) various sources have increased the amount of available data, especially concerning recruiting evaluation profiles of high-school athletes. Some data points, such as recruiting rankings and returning usage statistics, only had reliable data back to around 2010-2014. However, since rules and policies in college football have been changing so rapidly, we feel that **a 10 year window from 2014 to the present**, is adequate for making time-series predictions for the future. Additionally, **we considered only FBS teams** in our study, which are the top division teams in the NCAA.
## Stakeholders
- University athletic departments (for allocating NIL funds)
- College coaching staffs (for assembling rosters)
- Professional and amateur sports gamblers
## Key Performance Indicators (KPIs)
- Feature selection - identify key features that determine on-field outcomes
- Predict season win totals accurately - compare to baseline model of 6 win regular season (50/50 chance of winning each game)
- Highly explainable model that allows for actionable insights
## EDA + Feature Engineering
### Advanced Metrics
- We considered a wide array of features that measured (1) previous on-field success and (2) talent level of each team in each year. These include some self-explanatory categories such as wins, losses, etc. But we also studied some more advanced analytics including those listed and defined in [9] below:
   1. **ELO Rating:** As defined in [12] and named for physicist Arpad Elo, "*the Elo rating system is a method for calculating the relative skill levels of players in zero-sum games such as chess*" Here defined for each team over time, ELO involves setting and iteratively updating expectation values of winning for each team using a formula of the form:
      - $E_A = \frac{1}{1 + 10^{(\frac{R_B - R_A}{400})}}$, expected rating for team A
      - $E_B = \frac{1}{1 + 10^{(\frac{R_B - R_A}{400})}}$, expected rating for team B
  2. **ESPN Football Power Index (FPI)**: Proprietary formula for predicting matchups between teams based on a wide array of factors. 
   3. **Offensive and Defensive Success Rate:** As defined by [9], a successful play is when the offense gains (opposite for defense)
      - $\geq$ 50% of yards to go gained on 1st down
      - $\geq$ 70% of yards to go gained on 2nd down
      - $\geq$ 100% of yards to go gained on 3rd or 4th down.
   4. **Usages:** The % of production (pass and run plays on offense and total snaps on defense) from the previous season that is returning for the current season.
### Feature Engineering   
 1. **Talent-Level:** A rolling average of the last 4 team recruiting ratings. Since players only have 4 years of eligiblility, we average over 4 years.
 2. **Blue-Chip Ratio:** We calculated **blue-chip ratios**, a popular metric invented by Bud Elliot that measures the % of current players on the roster that were "blue-chip" recruits. These are recruits that were rated 4/5 or 5/5 stars in the 247Sports Composite Rankings [13]. It has been shown to be predictive of the set of teams that can win the national championsip.
 3. **Coach Win Percentage:** For every coach, we found the career average winning percentage leading up to a given season.
 4. **Recent Team Win Percentage:** For each team, we calculated the average winning percentage over the last 4 years to gauge recent success. This likely has high correlation with ELO.
 5. **Turnover Margin:** The total number of turnovers (interceptions + fumbles) gained each season minus the total turnovers lost.
 ### Feature Correlations
 - Below, we show correlations between some of these features:
![](images/correlation_heatmap.png "Feature Correlations")
- Next, we investigated some of of the features that seemed to be correlated with target, team win percentage:
![](images/high-correlated-with-win-pct.png "Scatterplots of Features")
- We also studied the relationships between features, particularly those that had to do with on-field performance vs. those that had to deal with team talent level:
![alt text](images/talent-vs-onfield-features.png "On Field vs. Talent Features")
- In college sports, coaches have tended to make a rather large difference in the success of a program. See a few examples below in the last 10 years,:
![alt text](images/school-win-pct-by-coach.png "Wins by Coach")
- We also saw that coach career winning percentage (which will obviously have some linear dependence with team winning percentage) is definitely correlated with team talent level (i.e. better coaches get better players):
![alt text](images/coach-win-pct.png "Coach win pct")
- Additionally, college sports has, historically, had several tiers of teams with a handful of teams seeing sustained success and many others having intermittent success. The features tend to have different relationships with the target depending on the tier of the team [14] 
## Modeling
### Approach 1: Regression over Season Level Features
- To predict winning percentage of each team, we used data from 2014-2023 with the features discussed above to perform regression focusing on 2014-2022 for training.
#### Feature Selection
- Using a random forest regressor, we measured the relative feature importance of our various features to see which ones reduced he impurity of the RF the most. ELO seemed to consistently dominate. *When predicting win percentage, this makes sense. If we were to use a different target such as points scored, other features would have higher relative importance.*
![feature_importance](images/feature_imporances.png "Feature Importance")
#### Modeling
- **Scaling:** We scaled the features to ensure that features like ELO that have extremely large values didn't arbitrarily dominate.
- **K-Fold Cross Validation:** We performed 5-fold cross validation for all of our models we describe below. We used **Mean Squared Error (MSE) as our loss metric** and took the average of the MSEs for each of our 5-folds. Our results are below:
![cross_val](images/cross-val-mses.png "Cross Validation")
- **Models:** We applied a variety of classical ML methods such as:
  1. Linear Regression
  2. Random Forest Regressor
  3. XGBoost
### Approach 2: Game by Game Time Series Approach
## Results
## References
[1] https://www.americangaming.org/research/state-gaming-map/ <br>
[2] https://cdn.ca9.uscourts.gov/datastore/opinions/2015/09/30/14-16601.pdf <br>
[3] https://www.ncaa.org/news/2021/6/30/ncaa-adopts-interim-name-image-and-likeness-policy.aspx <br>
[4] https://www.on3.com/nil/rankings/ <br>
[5] https://www.espn.com/college-football/fpi <br>
[6] https://www.espn.com/blog/statsinfo/post/_/id/122612/an-inside-look-at-college-fpi <br>
[7] https://247sports.com/season/2024-football/compositeteamrankings/<br>
[8] https://collegefootballdata.com/ <br>
[9] https://collegefootballdata.com/glossary <br>
[10] https://www.sports-reference.com/ <br>
[11] https://www.nytimes.com/athletic/5261402/2024/02/08/sec-payout-schools/ <br>
[12] https://en.wikipedia.org/wiki/Elo_rating_system <br>
[13] https://247sports.com/article/blue-chip-ratio-2023-college-football-16-teams-who-can-actually-win-a-national-title-211217111/ <br>
[14] https://www.cllct.com/sports-collectibles/memorabilia/how-much-did-your-school-get-to-appear-in-ea-college-football-25 <br>
