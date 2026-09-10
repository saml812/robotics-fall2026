# Mission 2

## Predictions

{'straight': 'The robot will be 0.45 meters forward relative to its starting position.', 'rotation': 'I predict its position will remain the same while its direction will rotate by 1.5 radians', 'curve': 'I predict a right-curving arc because the forward speed is positive, so the robot moves forward, and the turning speed is negative, which means the robot will rotate to the right.', 'curve_modified': 'This curve should be tighter and turn the other way because the turning speed is positive instead of negative, so the robot will turn left instead of right. The turn radius is also smaller because the robot turns more quickly, which means that the resulting motion will be a tighter left arc.'}

## Prediction Locks

{'straight': '2026-09-07T08:29:05.498965+00:00', 'rotation': '2026-09-07T08:31:30.388729+00:00', 'curve': '2026-09-07T08:35:34.626370+00:00', 'curve_modified': '2026-09-07T08:40:56.974256+00:00'}

## Motion Comparison

Looking at the straight motion trial. It was pretty accurate. I predicted that the robot would move forward in a straight line, which, in fact, did happen, as the table reports 0 degrees of change in direction. The robot traveled 0.428 meters, which is fairly close to the predicted path of 0.45 m. I believe that the small difference is due to the simulation updates and timing.

## Measurement Explanation

For the Curve Modified trial, the estimated traveled path is 0.459 m, while the start‑to‑end distance is only 0.365 m. They describe different things because the estimated traveled path measures the entire curved arc the robot actually drove. The start‑to‑end distance measures only the straight‑line displacement between its starting point and its final position. Since the robot followed a curved path instead of a straight line, the straight‑line distance is always shorter than the actual path length.

## Safety Explanation

The command guard checks every proposed driving command on /student_cmd_vel before it can reach the robot. It acts like a filter that blocks any speed values that are too extreme to prevent erratic motion.

The final zero command ensures that the robot completely stops when it finishes a trial. For example, the robot reaches its position, so the final zero command will set both its forward and turning speed to zero to stop the robot from continuing. 

The timeout is needed if a program crashes, freezes, or loses communication while the robot is still moving. The guard automatically sends a stop command half a second later to prevent the robot from driving uncontrollably.

## Modified Settings

{'linear_x': 0.12, 'angular_z': 0.6, 'duration': 4.0}
