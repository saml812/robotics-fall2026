# Mission 1

## Command Path Explanation

A proposed command travels on /student_cmd_vel. The guard /course_cmd_vel_guard subscribes to that topic to apply a safety check and then publishes the new command on /cmd_vel. These two topics are separate because one is for getting student commands, and the other is for filtering those commands before they reach the robot.

## Graph Explanation

A ROS 2 graph shows a map of nodes and how they communicate with each other through topics. For example, the node /ros_gz_bridge publishes distance readings on the topic /scan, and the node /course_evidence_collector subscribes to /scan to receive the readings.

## Guided Checks

{'bridge_info': True, 'command_topics': True, 'guard_info': True, 'node_list': True, 'scan_info': True, 'scan_message': True}

## Scan Observation

I found a couple of inf values, which represent that the sensor didn't detect any obstacle within its maximum distance of 3.5. 

## Tools Explanation

Gazebo simulates the physical environment; it deals with motion, collisions, and sensor outputs based on physics. RViz is used for visualizing ROS 2 data such as a robot's position and sensor readings.
