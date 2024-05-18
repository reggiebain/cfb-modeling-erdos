# Jimmys and Joes vs X’s and O’s
### *Predicting results in college sports analyzing talent accumulation and on-field success. A 2024 Erdös Institute Project.*
## Authors 
- Reggie Bain &nbsp;<a href="https://www.linkedin.com/in/reggiebain/"><img src="https://upload.wikimedia.org/wikipedia/commons/c/ca/LinkedIn_logo_initials.png" alt="LinkedIn" style="height: 1em; width:auto;"/></a> &nbsp; <a href="https://github.com/reggiebain"> <img src="https://upload.wikimedia.org/wikipedia/commons/9/91/Octicons-mark-github.svg" alt="GitHub" style="height: 1em; width: auto;"/></a>
- Reid Harris &nbsp;<a href="https://www.linkedin.com/in/reid-harris-71233a1b0/"><img src="https://upload.wikimedia.org/wikipedia/commons/c/ca/LinkedIn_logo_initials.png" alt="LinkedIn" style="height: 1em; width:auto;"/></a> &nbsp; <a href="https://github.com/ReidHarris"> <img src="https://upload.wikimedia.org/wikipedia/commons/9/91/Octicons-mark-github.svg" alt="GitHub" style="height: 1em; width: auto;"/></a>
- Tung Nguyen &nbsp;<a href="https://www.linkedin.com/in/tungprime/"><img src="https://upload.wikimedia.org/wikipedia/commons/c/ca/LinkedIn_logo_initials.png" alt="LinkedIn" style="height: 1em; width:auto;"/></a> &nbsp; <a href="https://github.com/tungprime"> <img src="https://upload.wikimedia.org/wikipedia/commons/9/91/Octicons-mark-github.svg" alt="GitHub" style="height: 1em; width: auto;"/></a> 
## Summary
In this project, we analyze a variety of college football related data in an effort to build a model that can predict on-field success. By considering both talent accumulation and recent on-field results, we aim for a model to predict relevant results for sports betting.
## Background
Recent legislation has completely changed the landscape of college sports, a multi-billion dollar business with deep roots in American sports culture. With the recent legalization of sports betting in many states and the SCOTUS O’Bannon ruling that allows athletes to be paid through so-called “Name-Image-Likeness (NIL)” deals, evaluating talent and projecting results in college sports, especially for the purpose of sports betting, is an increasingly interesting problem. We are interested in building a model to project on-field results in college football using a variety of features including an assessment of the talent level of teams as well as recent performance statistics. Our data will be scraped from various sources including the College Football Database, 247 Sports, On3, and ESPN.
## Dataset(s)
Our dataset comes from a variety of sources including On3, ESPN, 24/7 Sports, and The College Football Database. We have used APIs and web scraping techniques to identify a wide array of college football features including, but not limited to: team ELO ratings, conference strength ratings, team records from 2000-present, team recruiting rankings, player recruiting rankings, position group recruiting rankings, along with team performance stats and the stats of the players that returned to a team in a given year.
## Stakeholders
- University athletic departments (for allocating NIL funds)
- College coaching staffs (for assembling rosters)
- Professional and amateur sports gamblers
## Key Performance Indicators (KPIs)
- Feature selection - identify key features that determine on-field outcomes
- Predict season win totals accurately - compare to baseline model of 6 win regular season (50/50 chance of winning each game)
- Highly explainable model that allows for actionable insights
## EDA + Feature Engineering
- We considered a wide array of features that measured (1) previous on-field success and (2) talent level of each team in each year. These include some self-explanatory categories such as wins, losses, etc. But we also studied some more advanced analytics including those listed and defined in [5] below:
   1. **Offensive and Defensive Predicted Points Added:** The average for a team in a given year of the points expected to be scored before and after a given play. (off_ppa, def_ppa)
   2. **Offensive and Defensive Success Rate:** As defined by [5], a successful play is when the offense scored OR at least 50% of yards to go gained on 1st down OR 70% of yards to go gained on 2nd down OR 100% of yards to go gained on 3rd or 4th down. (off_success_rate, def_success_rate)
   3. **Offensive and Defensive Explosiveness:** The predicted points added for plays classified successful (see above). (off_explode, def_explode)
   4. **Usages:** The % of pass/run plays from that season where current players were involved. (usage, pass_usage, run_usage)
 - We also calculated "blue-chip ratios," a popular metric invented by Bud Elliot that measures the % of current players on the roster that were "blue-chip" recruits. These are recruits that were rated 4/5 or 5/5 stars in the 247Sports Composite Rankings [6]
 - Below, we show correlations between some of these features:
![Alt text](images/correlation_heatmap.png "Feature Correlations")
- Next, we investigated some of of the pairs of features that seemed to be correlated with each other and/or with win or loss percentage:
![](images/high-correlated-with-win-pct.png "Scatterplots of Features")

## Modeling
## Results
## References
[1] https://www.americangaming.org/research/state-gaming-map/ <br>
[2] https://www.ncaa.org/news/2021/6/30/ncaa-adopts-interim-name-image-and-likeness-policy.aspx <br>
[3] https://cdn.ca9.uscourts.gov/datastore/opinions/2015/09/30/14-16601.pdf <br>
[4] https://www.espn.com/blog/statsinfo/post/_/id/122612/an-inside-look-at-college-fpi
[5] https://collegefootballdata.com/glossary 
[6] https://247sports.com/season/2024-football/compositeteamrankings/
