# Final reflection

Respond to any or all of these prompts:

1. What did this activity make you think about regarding your own interests in robotics, computing, engineering, or related work?
2. How did this activity affect your motivation to do similar kinds of work in the future?
3. What value do you see in connecting technical or computing work with human, ethical, or societal considerations?
4. What stood out to you about the activity, and why?
5. Is there anything else you would like to share about your experience with the activity?

## Response

What stood out most was how often the "best" answer changed depending on what I measured. DFS looked efficient in Mission 1 because it expanded fewer cells, but on the robot it failed twice: its long, zig-zagging route forced tight turns next to walls until the controller gave up. Planning took about a millisecond, while driving took over a minute, so the quality of the route mattered far more than the speed of the search. That changed how I think about algorithm efficiency in robotics. The cost that matters is the cost of the whole journey, not just the computation.

Mission 3 made me think about the human side of robotics. A collision-free route is not automatically an acceptable one. A person can be safe and still feel crowded by a robot passing within arm's length. I was surprised that a weak personal-space setting actually made the robot spend more time near the person than doing nothing, and that the stronger setting gave more space without any time cost. It showed me that social behaviour has to be tested, not assumed, and that the numbers (0.75 m, the field strengths) are design choices someone has to explain.

_Word count: 197_
