# Week 5: Sensors, Noise, and Uncertainty

- course_id: CSCI39536
- email: sam.lin45@login.cuny.edu
- name: Sam Lin

## concepts.observation

When increasing the noise, the variance and standard deviation increased. On the Measurement sequence plot, there is an increase in the signals. When increasing the bias, the mean and the median increase. 

## final.course_reflection

This lab changed how I think about my own interests in robotics. Before this week, I mostly treated a sensor reading as a truth. Now I see that every measurement carries noise, bias, and dropout, and the interesting work is deciding how much to trust a number before acting on it.
It increased my motivation to keep doing this kind of work because careful technical decisions have direct consequences for people's safety and trust. 
Tuning the filter window and fusion weight and watching RMSE and delay actually respond felt like real engineering; each choice had a measurable trade-off.
What stood out most was Mission 3, and how the same estimation problem had two different right answers depending on the scenario. A warehouse robot may not want an unnecessary stop because it costs time, but an assistive robot near a person cannot afford a false-safe move. That reframed choosing thresholds as partly an ethical decision, not purely a technical one.

## final.synthesis

In this lab, I explored what a measurement tells us, how we estimate from it, and who is affected when those estimates are wrong. 
In mission 1, I analyzed how noise causes measurements to vary, while bias introduces a systematic offset. Increasing the sample size reduces variance but does not eliminate bias, demonstrating that precision does not necessarily mean accuracy. 
In mission 2, I evaluated moving average and median filters to reduce measurement errors. Although a moving average smooths noise, a larger window increases response delay when conditions change abruptly. For example, increasing the window size from 3 to 11 raised the delay from 1.30 s to 2.05 s. To balance accuracy and responsiveness, I selected a median filter with a window size of 3 and a fusion weight of 0.50, achieving the lowest RMSE of 0.132 m with an acceptable delay of 0.70 s. 
Mission 3 demonstrated that the best estimation policy depends on the application and the consequences of errors. In the warehouse scenario, my revised policy reduced unnecessary stops from 4.08% to 0%. In contrast, a different policy for the assistive robot maintained a 0% false-safe rate by using a higher threshold and a stop-on-missing rule. An unnecessary stop in a warehouse mainly costs time, while moving toward a person under uncertain conditions could cause serious injury.
The best policy is not simply the one that minimizes error; it is the one that balances accuracy, responsiveness, and safety according to the consequences of being wrong.

## mission_1.bias

0.0029 

## mission_1.bias_vs_variance

My prediction about what happens with a noisy sensor is correct. It should have a mean near 2.00 m, near-zero bias, and large variance. From the statstics, our mean = 2.0029 m, bias = 0.0029 m, variance = 0.0566 m², and median = 1.98 m. 
Bias and variance describe different failures because bias measures systematic displacement from the true value, while variance measures random scatter around the average. This sensor is unbiased but imprecise. A biased sensor would be consistently wrong but could still be precise; a noisy sensor can be correct on average but unreliable from reading to reading.

## mission_1.dropouts

6

## mission_1.mean

2.0029

## mission_1.median

1.98 

## mission_1.more_samples

More samples would not solve this sensor's main problem. It would reduce the standard error of the mean, making the average estimate more stable, but it would not reduce the sensor’s per-reading noise. The current standard deviation is about 0.238 m, with variance 0.0566 m², 6 dropouts, and 5 outliers. Even though bias is only 0.0029 m, the individual readings still scatter widely around 2.00 m. More samples would just add the same noisy distribution; they would not fix the main problem. 

## mission_1.outliers

5

## mission_1.prediction

I would predict that a biased sensor will have a sample mean shifted away from 2.00 meters and closer to the bias. The variance would remain small.
A noisy sensor will have a sample mean closer to 2.00 m because the random positive and negative errors will cancel each other out. Therefore, the bias is near zero, but there is large variance and a wide spread of readings. 
If the sensor is both biased and noisy, the mean will be shifted away from 2.00 m, and the spread will also be large. 
A biased sensor is inaccurate but can be precise, whereas a noisy sensor is imprecise but is unbiased.

## mission_1.prediction_draft

I would predict that a biased sensor will have a sample mean shifted away from 2.00 meters and closer to the bias. The variance would remain small.
A noisy sensor will have a sample mean closer to 2.00 m because the random positive and negative errors will cancel each other out. Therefore, the bias is near zero, but there is large variance and a wide spread of readings. 
If the sensor is both biased and noisy, the mean will be shifted away from 2.00 m, and the spread will also be large. 
A biased sensor is inaccurate but can be precise, whereas a noisy sensor is imprecise but is unbiased.

## mission_1.profile

noisy

## mission_1.robot_consequence

One robot decision this could change is when to stop 2.00 m before an obstacle. Because the sensor is noisy, a single reading might be 1.80 m or 2.30 m even when the true distance is 2.00 m. If the robot trusts that reading, it might stop too late and cause a collision. It could also stop too early and block the road. For a person nearby, they could get injured in a collision or be confused by the erratic stopping.

## mission_1.variance

0.0566 

## mission_2.comparison

For the three moving-average windows at a fixed weight of a = 0.25, the shortest window performed best. Window 11 gave RMSE = 0.1589 m, max error = 1.1806 m, and response delay = 2.05 s. Window 7 improved to RMSE = 0.1502 m, max error = 1.1614 m, and delay = 1.30 s. Window 3 gave the lowest RMSE and max error of the moving-average set: RMSE = 0.1420 m, max error = 1.1086 m, and delay = 1.30 s. So window 3 reduced RMSE by about 0.0168 m and max error by about 0.0720 m compared with window 11, while cutting delay by 0.75 s. Window 3 also beat window 7 by about 0.0082 m RMSE and 0.0529 m max error, with no delay penalty.

For the matched median/moving-average comparison at window 3 and weight A = 0.25, the moving average gave RMSE = 0.1420 m, max error = 1.1086 m, MAE = 0.0781 m, and delay = 1.30 s, while the matched median gave RMSE = 0.1407 m, max error = 1.2336 m, MAE = 0.0759 m, and delay = 1.30 s. The matched median slightly improved average error, reducing RMSE by about 0.0013 m and MAE by about 0.0022 m, but it increased max error by about 0.1250 m compared with the moving average. Because the delay was identical at 1.30 s, the difference came from the filter method rather than responsiveness: the median smoothed average error a little better, but it did not reject the worst-case error as well as expected in this run.

## mission_2.fusion_choice

With median window 3 and different weights on Sensor A, weight A = 0.25 gave RMSE = 0.1407 m, max error = 1.2336 m, MAE = 0.0759 m, delay = 1.30 s, and availability = 100%. Weight A = 0.50 gave RMSE = 0.1324 m, max error = 1.3790 m, MAE = 0.0775 m, delay = 0.70 s, and availability = 100%. Weight A = 0.75 gave RMSE = 0.1457 m, max error = 1.5245 m, MAE = 0.0900 m, delay = 0.60 s, and availability = 100%. Weight A = 0.25 failed the delay target at 1.30 s, and weight A = 0.75 had the worst RMSE, max error, and MAE because it trusted Sensor A too much. I selected weight A = 0.50 because it achieved the lowest RMSE, 0.1324 m, while keeping max error at 1.3790 m and delay at 0.70 s, both within the targets. This weight balances the sensors’ limitations since Sensor A is fast but noisy and outlier-prone, so adding more weight to it raises error, while Sensor B is steadier but biased and samples only every fourth step, so adding weight to that sensor adds more bias and delay. Weight A = 0.50 uses enough of A for responsiveness but enough of B to reduce A’s noise.

## mission_2.manual_average

4.17

## mission_2.manual_fusion

2.25

## mission_2.manual_median

2.3

## mission_2.prediction_draft

The moving-average window has a fusion weight of 0.25. Window 3 should track the 6.00 s change quickly but let outliers through and raise max error. Window 7 should reduce noise but add delay, and Window 11 should be the smoothest but slowest, with the worst delay. 
The median window 3 with varying fusion weight. At weight A = 0.25, the median should reject the 8.0 m outlier better than the moving average at the same window. At weight A = 0.50, giving more weight to Sensor B should reduce Sensor A’s noise but add bias because B is steadier yet biased and samples every fourth time step. At weight A = 0.75, giving more weight to Sensor A should improve responsiveness but let more of A’s noise and outliers through.

## mission_2.responsiveness

The longest moving-average window, window 11, had the largest delay, 2.05 s, while windows 7 and 3 both had 1.30 s. That means the longer smoothing window made the system slower to react to the 6.00 s change by about 0.75 s, and it did not improve RMSE or max error in this data. The fusion weight also affected the delay. The median window 3, weight A = 0.25 had a delay of 1.30 s, weight A = 0.50 had a delay of 0.70 s, and weight A = 0.75 had a delay of 0.60 s. Giving more weight to the faster Sensor A reduced delay, but at weight A = 0.75 the RMSE rose to 0.1457 m and max error rose to 1.5245 m, showing that more responsiveness also let more noise and outliers through.

For a nearby person, a delay of 2.05 s could mean the robot reacts late to an obstacle or person, increasing collision risk or causing a very close stop. A very short delay with too little smoothing could instead make the robot twitchy and react to a single bad Sensor A reading, causing erratic movement and unnecessary braking.

## mission_2.selected

4

## mission_3.Assistive.prediction_draft

I predict that requiring two confirmations will slightly slow the STOP decision in the stationary_danger and fast_approach scenarios, raising delay a little, while false-safe stays near zero and unnecessary stops stay similar — the extra confirmation trades a small delay for more certainty before committing to a stop.

## mission_3.Warehouse.prediction_draft

I predict scenarios with missing readings and with low outliers or dropouts from Sensor A will challenge this policy. Because the missing-data rule is STOP, any scenario where both current readings are missing will force a stop. This is safe but can create unnecessary stops and delays. Low outliers may also trigger a premature STOP, while high outliers could push the estimate above the stop boundary and create a false-safe MOVE. Compared with a previous policy, I expect false-safe events to remain relatively low because the stopping threshold equals the 0.75 m safety distance, but unnecessary stops should be higher when readings are dropped out. The detection delay should be short because only one reading at or below the stop boundary is required before STOP.

## mission_3.context_comparison

My two final policies differ most in stopping threshold, caution margin, and the missing-data rule. The warehouse uses a 0.75 m threshold with no margin and "Insufficient evidence" on missing data, generating 0.62% false-safe, 0% unnecessary stops, and 0.25 s delay. It refrains from stopping to save time. The assistive robot uses a higher 0.95 m threshold with a 0.2 m margin, "Stop" on missing data, and two confirmations, giving 0% false-safe, 2.70% unnecessary stops, and 0.10 s delay. It defaults to stops and stops earlier when uncertain because a missed stop could hurt a person, whereas a warehouse delay only costs time.

## mission_3.error_costs

In the warehouse, a false-safe MOVE risks damaging racks or equipment, and unnecessary stops delay work. Both costs land on operators and the facility as lost throughput. My revised policy (margin 0.0, "Insufficient evidence" on missing data) removed unnecessary stops from 4.08% to 0.00%, while false-safe held at 0.62% and delay rose from 0.10 s to 0.25 s. 

In the assistive setting, a false-safe MOVE can injure the person, so the cost is the user, while unnecessary stops block their path and make the robot feel untrustworthy. My policy kept false-safe at 0.00% and unnecessary stops at 2.70%, and the two-confirmation only raised delay from 0.05 s to 0.10s.

## mission_3.limitations

These seven tests establish that my policies satisfy the criteria under simulated conditions of zero dangerous-command events, 0% assistive false-safe, 0.62% warehouse false-safe, and detection delays of 0.10–0.25 s, all within limits for noise, dropout, conflicting sensors, and an abrupt approach. What they do not establish is real-world safety and the environment changing. The simulation models only measurement and decision logic. It assumes fixed noise and outlier distributions, and removes physical robot dynamics, actuation and processing lag, dynamic obstacles, and people. Before deployment, I would consult a warehouse operations manager and, for the assistive robot, an occupational therapist, and add one physical test to run the actual sensor and robot in a controlled space and have a person throw an object that enters the robot's path mid-motion to measure the true detection delay and stopping distance against the simulated 0.10–0.25 s.
