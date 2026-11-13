The main lesson is that a model's response is not always correct and perfect, and it only becomes useful robot behavior after it is checked against the robot's capabilities, what is actually visible, and what happens when it acts.

In Mission 1 the language model answered fluently but invented facts. For the clear request it said the robot starts at the shelf (it starts at base) and that the cup is empty, although no image was taken. For "pick up the cup" it quietly swapped in a different task instead of saying the robot has no gripper. My revised request stated the start, limited the skills and banned guessing, and produced a clean four-step navigate-inspect-report-stop plan that fits the capability card.

In Mission 2 the vision model called the drawing compass a tape measure for all three questions. Adding the missing goal (mark a circle) moved it toward a circle-drawing tool, but it answered "pencil" and repeated the features I had put in my own question.

In Mission 3 none of the six maze runs reached (11,1). The wall check kept every run safe (blocked moves left the robot in place), but it does not plan. At (1,1), with RIGHT free and the allowed list "DOWN, RIGHT, STOP", the model chose DOWN or STOP whatever my rule said. Banning STOP removed the pauses (0 instead of 22) without producing progress.

This show that  these small models do not reliably follow conditional instructions or ground claims in the image, so prompting alone cannot make them dependable. A real robot would need a validator, a planner and better observations around the model.