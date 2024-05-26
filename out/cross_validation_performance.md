| model                   |   avg_mse |   avg_rmse |   pct_improve_mse |   pct_improve_rmse |
|:------------------------|----------:|-----------:|------------------:|-------------------:|
| Baseline Naive Forecast | 0.0484019 |   0.220004 |            0      |             0      |
| LinearRegression        | 0.0307367 |   0.175319 |           36.497  |            20.3112 |
| KNeighborsRegressor     | 0.0380674 |   0.195109 |           21.3515 |            11.316  |
| RandomForestRegressor   | 0.0329434 |   0.181503 |           31.9378 |            17.5002 |
| XGBRegressor            | 0.0382383 |   0.195546 |           20.9983 |            11.1171 |
| LSTM                    | 0.0337128 |   0.18361  |           30.3482 |            16.5424 |