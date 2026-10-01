# mission_1 Submission

- Name: Sam Lin
- Section: (not provided)

## Explanations

### prediction

With too little Kp, I expect the arm to respond sluggishly and slowly: it will move slowly toward the target, may never reach it, and will likely stop short. With too little Kd, I expect the arm to overshoot the target and oscillate around it. The motion will be underdamped, so it should take a longer time to settle.

### tuning_analysis

I predicted that too little Kp would make the arm sluggish and leave it short of the target, while too little Kd would cause overshoot and oscillation. That matched the testing: with low Kp = 1.0, the shoulder sagged and held a steady error, and with low Kd = 0.6, both joints oscillated around the target before settling. I changed both controllers to Kp = 6.0, Ki = 0.9, Kd = 1.3 separately, one at a time. Raising Kp​ made each joint move faster; increasing Kd ​damped the overshoot and made it settle faster, and the small Ki​ corrected the remaining steady offset such that the tip gap showed 0px.
Gravity compensation made it much faster for both joints to settle. It reduced the steady command needed to hold the second link, so the shoulder no longer sagged under gravity and needed less integral action to correct the error.