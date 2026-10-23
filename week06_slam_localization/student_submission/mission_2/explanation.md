# Mission 2

## Comparison

Mission 1 took 30 minutes, while Mission 2 took 40 minutes. Despite the extra 10 minutes, the data show Mission 2 mapped more of the space: the known fraction increased from 55.92% to 64.35%, and the known area increased from 81.46 m² to 92.25 m². Mission 2 also had less noise, as shown by the speckle fraction dropping from 4.09% to 3.4%. However, Mission 1 gave much more useful coverage for the time spent; its rate was 2.72 m²/min, whereas Mission 2 dropped to 2.31 m²/min.

My prediction was partially supported. I predicted Mission 2 would take longer and map more area, which happened. However, I predicted it would produce a "clearer and more accurate map," which is contradicted by the Quality score dropping from 85.4 to 79.9. The back-and-forth route traded speed and structural integrity for total coverage. By spending more time maneuvering, the robot accumulated more wheel odometry drift, causing the map quality to degrade even though it saw more square meters.


## Map Choice

I would actually trust the Mission 1 map more for a later navigation task, despite its missing areas.

Visible Evidence: In Mission 1, the walls were generally thin, straight, and single-lined. In Mission 2, while it had more map coverage, the walls have overlapped and duplicated. The long horizontal corridor in Mission 2 is thick and jagged. The vertical wall dividing the top-center room is heavily smeared or doubled on its right side, and the bottom-right walls look skewed and misaligned.

For a robot to navigate safely, having straight, single-line walls is better than having a wider known area but smeared, double walls. Double walls cause the robot's path planner to think there are obstacles where there are none, or to misjudge the width of doorways and corridors.

One limit of what these images/numbers can prove is that 2D images and algorithmic metrics cannot prove the true 3D safety of the map or prove whether the robot successfully drove under the tables without colliding with the countertop.

## Strategy.Original Prediction

My new route will involve driving in back-and-forth (lawnmower) sweeps instead of wandering randomly into rooms like in my first route. I will start by driving a large loop around the interior perimeter. After completing this loop, I will enter the rooms to perform a thorough lawnmower sweep. Additionally, when passing the tables, I will deliberately go underneath them. I predict this new route will produce a significantly clearer and more accurate map, though it will likely take longer to complete in real time because I am prioritizing deliberate data collection and loop closure over direct, point-to-point driving.

## Strategy.Prediction Draft

My new route will involve driving in back-and-forth (lawnmower) sweeps instead of wandering randomly into rooms like in my first route. I will start by driving a large loop around the interior perimeter. After completing this loop, I will enter the rooms to perform a thorough lawnmower sweep. Additionally, when passing the tables, I will deliberately go underneath them. I predict this new route will produce a significantly clearer and more accurate map, though it will likely take longer to complete in real time because I am prioritizing deliberate data collection and loop closure over direct, point-to-point driving.
