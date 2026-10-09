# Mission 3

## Assistive.prediction_draft

I predict that requiring two confirmations will slightly slow the STOP decision in the stationary_danger and fast_approach scenarios, raising delay a little, while false-safe stays near zero and unnecessary stops stay similar — the extra confirmation trades a small delay for more certainty before committing to a stop.

## Warehouse.prediction_draft

I predict scenarios with missing readings and with low outliers or dropouts from Sensor A will challenge this policy. Because the missing-data rule is STOP, any scenario where both current readings are missing will force a stop. This is safe but can create unnecessary stops and delays. Low outliers may also trigger a premature STOP, while high outliers could push the estimate above the stop boundary and create a false-safe MOVE. Compared with a previous policy, I expect false-safe events to remain relatively low because the stopping threshold equals the 0.75 m safety distance, but unnecessary stops should be higher when readings are dropped out. The detection delay should be short because only one reading at or below the stop boundary is required before STOP.

## context_comparison

My two final policies differ most in stopping threshold, caution margin, and the missing-data rule. The warehouse uses a 0.75 m threshold with no margin and "Insufficient evidence" on missing data, generating 0.62% false-safe, 0% unnecessary stops, and 0.25 s delay. It refrains from stopping to save time. The assistive robot uses a higher 0.95 m threshold with a 0.2 m margin, "Stop" on missing data, and two confirmations, giving 0% false-safe, 2.70% unnecessary stops, and 0.10 s delay. It defaults to stops and stops earlier when uncertain because a missed stop could hurt a person, whereas a warehouse delay only costs time.

## error_costs

In the warehouse, a false-safe MOVE risks damaging racks or equipment, and unnecessary stops delay work. Both costs land on operators and the facility as lost throughput. My revised policy (margin 0.0, "Insufficient evidence" on missing data) removed unnecessary stops from 4.08% to 0.00%, while false-safe held at 0.62% and delay rose from 0.10 s to 0.25 s. 

In the assistive setting, a false-safe MOVE can injure the person, so the cost is the user, while unnecessary stops block their path and make the robot feel untrustworthy. My policy kept false-safe at 0.00% and unnecessary stops at 2.70%, and the two-confirmation only raised delay from 0.05 s to 0.10s.

## limitations

These seven tests establish that my policies satisfy the criteria under simulated conditions of zero dangerous-command events, 0% assistive false-safe, 0.62% warehouse false-safe, and detection delays of 0.10–0.25 s, all within limits for noise, dropout, conflicting sensors, and an abrupt approach. What they do not establish is real-world safety and the environment changing. The simulation models only measurement and decision logic. It assumes fixed noise and outlier distributions, and removes physical robot dynamics, actuation and processing lag, dynamic obstacles, and people. Before deployment, I would consult a warehouse operations manager and, for the assistive robot, an occupational therapist, and add one physical test to run the actual sensor and robot in a controlled space and have a person throw an object that enters the robot's path mid-motion to measure the true detection delay and stopping distance against the simulated 0.10–0.25 s.
