# Mission 3

## Data To Command

The front_distance() function takes the raw LiDAR readings and calculates the angle of each reading, keeping only those for which abs(angle) <= half_width_radians, the value is finite, and the angle is greater than zero. It then returns the nearest valid distance from the list of valid LiDAR distances. 

The decide_velocity will take that nearest valid distance along with stop_distance and forward speed and make a decision on whether the robot should stop or not. If the distance is None or less than or equal to the stop_distance, it returns 0.0 to stop. Otherwise, it returns the forward speed bounded between 0.0 and 0.18 m/s.

Essentially,  the first function extracts a reliable measurement from noisy sensor data, and the second function translates that measurement into a concrete action.

## Missing Data Safety

The robot should stop because an invalid front measurement, such as inf or nan, does not guarantee that the space is clear. Treating them as clear would be unsafe because the robot could blindly drive into undetected obstacles.

## System Layers

The two functions are called in the obstacle_guard.py. The ROS node obstacle_guard subscribes to the /scan topic, passing each incoming scan to the front_distance() function and then to decide_velocity() to compute a forward speed, and then publishes that speed as a Twist message on the/student_cmd_vel topic.

The command guard /course_cmd_vel_guard subscribes to the/student_cmd_vel topic to apply safety checks and then publishes the final command on /cmd_vel. The simulator bridge picks up /cmd_vel and drives the robot in Gazebo.
