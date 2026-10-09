# Mission 2

## comparison

For the three moving-average windows at a fixed weight of a = 0.25, the shortest window performed best. Window 11 gave RMSE = 0.1589 m, max error = 1.1806 m, and response delay = 2.05 s. Window 7 improved to RMSE = 0.1502 m, max error = 1.1614 m, and delay = 1.30 s. Window 3 gave the lowest RMSE and max error of the moving-average set: RMSE = 0.1420 m, max error = 1.1086 m, and delay = 1.30 s. So window 3 reduced RMSE by about 0.0168 m and max error by about 0.0720 m compared with window 11, while cutting delay by 0.75 s. Window 3 also beat window 7 by about 0.0082 m RMSE and 0.0529 m max error, with no delay penalty.

For the matched median/moving-average comparison at window 3 and weight A = 0.25, the moving average gave RMSE = 0.1420 m, max error = 1.1086 m, MAE = 0.0781 m, and delay = 1.30 s, while the matched median gave RMSE = 0.1407 m, max error = 1.2336 m, MAE = 0.0759 m, and delay = 1.30 s. The matched median slightly improved average error, reducing RMSE by about 0.0013 m and MAE by about 0.0022 m, but it increased max error by about 0.1250 m compared with the moving average. Because the delay was identical at 1.30 s, the difference came from the filter method rather than responsiveness: the median smoothed average error a little better, but it did not reject the worst-case error as well as expected in this run.

## fusion_choice

With median window 3 and different weights on Sensor A, weight A = 0.25 gave RMSE = 0.1407 m, max error = 1.2336 m, MAE = 0.0759 m, delay = 1.30 s, and availability = 100%. Weight A = 0.50 gave RMSE = 0.1324 m, max error = 1.3790 m, MAE = 0.0775 m, delay = 0.70 s, and availability = 100%. Weight A = 0.75 gave RMSE = 0.1457 m, max error = 1.5245 m, MAE = 0.0900 m, delay = 0.60 s, and availability = 100%. Weight A = 0.25 failed the delay target at 1.30 s, and weight A = 0.75 had the worst RMSE, max error, and MAE because it trusted Sensor A too much. I selected weight A = 0.50 because it achieved the lowest RMSE, 0.1324 m, while keeping max error at 1.3790 m and delay at 0.70 s, both within the targets. This weight balances the sensors’ limitations since Sensor A is fast but noisy and outlier-prone, so adding more weight to it raises error, while Sensor B is steadier but biased and samples only every fourth step, so adding weight to that sensor adds more bias and delay. Weight A = 0.50 uses enough of A for responsiveness but enough of B to reduce A’s noise.

## manual_average

4.17

## manual_fusion

2.25

## manual_median

2.3

## prediction_draft

The moving-average window has a fusion weight of 0.25. Window 3 should track the 6.00 s change quickly but let outliers through and raise max error. Window 7 should reduce noise but add delay, and Window 11 should be the smoothest but slowest, with the worst delay. 
The median window 3 with varying fusion weight. At weight A = 0.25, the median should reject the 8.0 m outlier better than the moving average at the same window. At weight A = 0.50, giving more weight to Sensor B should reduce Sensor A’s noise but add bias because B is steadier yet biased and samples every fourth time step. At weight A = 0.75, giving more weight to Sensor A should improve responsiveness but let more of A’s noise and outliers through.

## responsiveness

The longest moving-average window, window 11, had the largest delay, 2.05 s, while windows 7 and 3 both had 1.30 s. That means the longer smoothing window made the system slower to react to the 6.00 s change by about 0.75 s, and it did not improve RMSE or max error in this data. The fusion weight also affected the delay. The median window 3, weight A = 0.25 had a delay of 1.30 s, weight A = 0.50 had a delay of 0.70 s, and weight A = 0.75 had a delay of 0.60 s. Giving more weight to the faster Sensor A reduced delay, but at weight A = 0.75 the RMSE rose to 0.1457 m and max error rose to 1.5245 m, showing that more responsiveness also let more noise and outliers through.

For a nearby person, a delay of 2.05 s could mean the robot reacts late to an obstacle or person, increasing collision risk or causing a very close stop. A very short delay with too little smoothing could instead make the robot twitchy and react to a single bad Sensor A reading, causing erratic movement and unnecessary braking.

## selected

4
