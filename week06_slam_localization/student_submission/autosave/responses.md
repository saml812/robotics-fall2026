# Week 6: SLAM and Mapping

- name: Sam Lin
- email: sam.lin45@login.cuny.edu

## final.course_reflection

What stood out to me the most was how different route planning and navigation affected the overall quality and accuracy of the maps. Wandering somewhat randomly room by room gave a surprisingly better structural map than a deliberate sweep because of how odometry drift accumulated over the longer drive. This was counterintuitive and eye-opening, and it makes me wonder how modern robots that utilize SLAM best plan their routes to create the most accurate map possible while countering issues such as odometry drift.

What stood out to me the most was how different route planning and navigation affected the overall quality and accuracy of the maps. Wandering somewhat randomly room by room gave a surprisingly better structural map than a deliberate sweep because of how odometry drift accumulated over the longer drive. This was counterintuitive and eye-opening and makes me wonder how modern robots that utilize SLAM best plan their routes to create the most accurate map possible while countering issues such as odometry drift. This activity deepened my appreciation for the complexity of autonomous systems and motivated me to learn more about path planning algorithms, sensor fusion, and error correction in future engineering work. It showed me that in robotics, the smart algorithm can be unbound by poor physical motion estimates.

## final.synthesis

By combining LiDAR measurements with motion estimates, the TurtleBot3 creates an occupancy grid. However, these maps do have limitations in what the robot can know. The LiDAR can only detect line-of-sight obstacles, creating shadows beneath the tables. It cannot know if these spaces are truly empty without physically moving to scan from a new angle or moving underneath tables if possible.

Motion-estimate error is the other major issue. In Mission 1, the robot wandered, resulting in a lower known area (81.46 m²) but a high quality score of 85.4. The walls were mostly thin and straight, which shows small accumulated odometry drift. In Mission 2 which took around 40 minutes, the back and forth sweeping increased LiDAR coverage to 92.25 m². However, the longer driving time accumulated greater odometry error. The algorithm failed to fully correct this when revisits scanned areas. As a result, the central corridor became jagged, and the walls appeared doubled and skewed.

Therefore, I would trust Mission 1 more for a later navigation task. While Mission 2 has better overall coverage, its structural integrity is compromised by motion-estimate error. The "smeared" or doubled walls in Mission 2 could cause a path planner to misjudge doorway widths or perceive false obstacles, whereas Mission 1 provides a more reliable, albeit incomplete, geometric skeleton of the house.

## mission_1.drift_and_revisit

When I returned to previously scanned areas, the new scans generally lined up with the existing walls. However, the bottom right room is the most shifted and unaligned compared to the rest of the house. This shows accumulated odometry drift. As the robot drove down the long central corridor and turned into that room, small heading errors from wheel slip accumulated.  The SLAM algorithm mapped the entire room relative to a slightly skewed pose.

## mission_1.limitations

A large unmapped area remains in the bottom-center portion of the RViz map. My route only prioritized exploring inside the house instead of outside as well; therefore, the area remained unmapped. There are also unmapped areas where there was a table underneath. My route did not have the robot go under these tables. The LiDAR’s line of sight was blocked by the table legs and tabletops, creating unmapped areas in the two larger rooms. Because the TurtleBot3's 2D LiDAR scans at a single fixed height, it hits the table legs or the top surface and cannot see the space underneath.

## mission_1.route.original_prediction

Starting from the initial position at (-2, -0.5), I will first drive west into the large left room to navigate around the inner wall at (-6, -4) and map the left walls before returning to the starting point. From there, I will head east to explore the top-center room, then continue into the right wing to map both the bottom-right and top-right rooms before returning to the center corridor. I plan to revisit the starting point at (-2, -0.5) to compare current position and correct accumulated odometry drift. I predict the map will be weakest in the bottom-left room because of its tight geometry and sharp corners.

## mission_1.route.prediction_draft

Starting from the initial position at (-2, -0.5), I will first drive west into the large left room to navigate around the inner wall at (-6, -4) and map the left walls before returning to the starting point. From there, I will head east to explore the top-center room, then continue into the right wing to map both the bottom-right and top-right rooms before returning to the center corridor. I plan to revisit the starting point at (-2, -0.5) to compare current position and correct accumulated odometry drift. I predict the map will be weakest in the bottom-left room because of its tight geometry and sharp corners. 

## mission_2.comparison

Mission 1 took 30 minutes, while Mission 2 took 40 minutes. Despite the extra 10 minutes, the data show Mission 2 mapped more of the space: the known fraction increased from 55.92% to 64.35%, and the known area increased from 81.46 m² to 92.25 m². Mission 2 also had less noise, as shown by the speckle fraction dropping from 4.09% to 3.4%. However, Mission 1 gave much more useful coverage for the time spent; its rate was 2.72 m²/min, whereas Mission 2 dropped to 2.31 m²/min.

My prediction was partially supported. I predicted Mission 2 would take longer and map more area, which happened. However, I predicted it would produce a "clearer and more accurate map," which is contradicted by the Quality score dropping from 85.4 to 79.9. The back-and-forth route traded speed and structural integrity for total coverage. By spending more time maneuvering, the robot accumulated more wheel odometry drift, causing the map quality to degrade even though it saw more square meters.


## mission_2.map_choice

I would actually trust the Mission 1 map more for a later navigation task, despite its missing areas.

Visible Evidence: In Mission 1, the walls were generally thin, straight, and single-lined. In Mission 2, while it had more map coverage, the walls have overlapped and duplicated. The long horizontal corridor in Mission 2 is thick and jagged. The vertical wall dividing the top-center room is heavily smeared or doubled on its right side, and the bottom-right walls look skewed and misaligned.

For a robot to navigate safely, having straight, single-line walls is better than having a wider known area but smeared, double walls. Double walls cause the robot's path planner to think there are obstacles where there are none, or to misjudge the width of doorways and corridors.

One limit of what these images/numbers can prove is that 2D images and algorithmic metrics cannot prove the true 3D safety of the map or prove whether the robot successfully drove under the tables without colliding with the countertop.

## mission_2.strategy.original_prediction

My new route will involve driving in back-and-forth (lawnmower) sweeps instead of wandering randomly into rooms like in my first route. I will start by driving a large loop around the interior perimeter. After completing this loop, I will enter the rooms to perform a thorough lawnmower sweep. Additionally, when passing the tables, I will deliberately go underneath them. I predict this new route will produce a significantly clearer and more accurate map, though it will likely take longer to complete in real time because I am prioritizing deliberate data collection and loop closure over direct, point-to-point driving.

## mission_2.strategy.prediction_draft

My new route will involve driving in back-and-forth (lawnmower) sweeps instead of wandering randomly into rooms like in my first route. I will start by driving a large loop around the interior perimeter. After completing this loop, I will enter the rooms to perform a thorough lawnmower sweep. Additionally, when passing the tables, I will deliberately go underneath them. I predict this new route will produce a significantly clearer and more accurate map, though it will likely take longer to complete in real time because I am prioritizing deliberate data collection and loop closure over direct, point-to-point driving.
