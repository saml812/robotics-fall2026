# Mission 1

## Drift And Revisit

When I returned to previously scanned areas, the new scans generally lined up with the existing walls. However, the bottom right room is the most shifted and unaligned compared to the rest of the house. This shows accumulated odometry drift. As the robot drove down the long central corridor and turned into that room, small heading errors from wheel slip accumulated.  The SLAM algorithm mapped the entire room relative to a slightly skewed pose.

## Limitations

A large unmapped area remains in the bottom-center portion of the RViz map. My route only prioritized exploring inside the house instead of outside as well; therefore, the area remained unmapped. There are also unmapped areas where there was a table underneath. My route did not have the robot go under these tables. The LiDAR’s line of sight was blocked by the table legs and tabletops, creating unmapped areas in the two larger rooms. Because the TurtleBot3's 2D LiDAR scans at a single fixed height, it hits the table legs or the top surface and cannot see the space underneath.

## Route.Original Prediction

Starting from the initial position at (-2, -0.5), I will first drive west into the large left room to navigate around the inner wall at (-6, -4) and map the left walls before returning to the starting point. From there, I will head east to explore the top-center room, then continue into the right wing to map both the bottom-right and top-right rooms before returning to the center corridor. I plan to revisit the starting point at (-2, -0.5) to compare current position and correct accumulated odometry drift. I predict the map will be weakest in the bottom-left room because of its tight geometry and sharp corners.

## Route.Prediction Draft

Starting from the initial position at (-2, -0.5), I will first drive west into the large left room to navigate around the inner wall at (-6, -4) and map the left walls before returning to the starting point. From there, I will head east to explore the top-center room, then continue into the right wing to map both the bottom-right and top-right rooms before returning to the center corridor. I plan to revisit the starting point at (-2, -0.5) to compare current position and correct accumulated odometry drift. I predict the map will be weakest in the bottom-left room because of its tight geometry and sharp corners. 
