# mission_3 Submission

- Name: Sam Lin
- Section: (not provided)

## Explanations

### technical_analysis

I predicted that increasing speed and using too little Kd control would raise tracking error and shrink pedestrian clearance. The drive shows that at 0.34 m/s with heading Kp = 2.7, Ki = 0.15, Kd = 0.65, the robot stayed within the limits, with mean path error 0.01 m, max path error 0.07 m, closest approach 0.36 m, and all 4 waypoints reached. 

The robot computes the next route point by taking the vector from its current estimated pose to the next waypoint and turning that into a desired heading, θ desired = atan2(Δy,Δx). The heading error is θ desired − θ current. The PID changes steering based on that error. Kp reacts to the current heading error, Ki accumulates past heading error to remove a persistent bias, and Kd damps the rate of change so the robot does not oscillate and helps it settle faster. The output commands the steering or wheel-speed difference. The green and orange paths showed that if the wheel-radius estimate is wrong, odometry converts encoder ticks into the wrong distance. The controller can be well tuned and still follow the wrong physical path because it is steering relative to a drifted pose estimate; thus, the estimated path will be off.

### human_centered_analysis

The consequential failure is the robot coming too close to a pedestrian or failing to stop, which could cause injury or force someone to move out of the way. I would require at least 0.35 m clearance in normal operation and a lower speed in crowded areas, which can result in slower deliveries but protects pedestrians from getting hurt.

Responsibility belongs to the engineering team because they choose the gains, speed limits, route planning rules, and verify testing before the robot is allowed around people.