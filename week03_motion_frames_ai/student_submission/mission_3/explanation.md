# Mission 3

## Ai Disclosure

I used the AI assistant, DeepSeek, to draft the initial build_pattern implementation, propose the student tests, explain Python syntax such as list[Segment] and Segment(...), and to identify possible omissions and errors. I personally reviewed the generated code and kept the supplied Segment class unchanged. I added import math, added the ValueError guard for unknown pattern names, derived omega = 0.70 rad/s, v = R * omega = 0.21 m/s, and duration = (π/4) / omega ≈ 1.121997 s, and kept the segment order [+ω, −ω, +ω, −ω]. I did not add a final stop segment because the wrapper publishes the final zero and the evaluator verifies it. I wrote and saved test/test_student_pattern.py with two tests: one for geometry and limits, one for order and no-stop-segment behavior. I ran the python3 scripts/evaluate_ai_pattern.py and verified the reported results.

## Assigned Pattern

alternating_arcs

## Assumptions

The AI assumed that the robot body frame has +x forward, +y left, and positive angular_z meaning a left turn. It assumed the units to be m/s for linear_x, rad/s for angular_z, and seconds for duration. If asked to explain unfamiliar syntax, the assistant would say that list[Segment] is a Python type hint and Segment(...) constructs the existing data object using keyword arguments.

The AI assumed that Segment is already defined or imported in pattern.py, that pattern_node.py repeatedly publishes each segment for its full duration and then sends zero velocity, and that positive angular velocity is left. The AI assumed that each segment is positive and at most 30 s, and the total time is at most 60 s.

## Evidence Analysis

The important tests establish that the implementation matches the assigned alternating-arcs pattern. pattern.py implementation was found, and test/test_student_pattern.py was found to have passed, so the required files exist. Student test methods reported 2 found; 2 required, so my two pattern-specific tests were discovered. All automated tests reported 9 passing; 9 required, so the seven tests plus my two student tests all passed. Assigned geometry passed, confirming the four +45°, −45°, +45°, −45° arcs, radius 0.30 m, and final heading matched the specification. Command limits passed, confirming |v| ≤ 0.22 m/s, |ω| ≤ 0.80 rad/s, each segment ≤ 30 s, and total ≤ 60 s. Stop decision passed, confirming the wrapper owns the final stop. Live motion and stop passed, which confirms the simulated motion-and-stop check matched.

My geometry test checked four segments, forward speed, radius R = |v/ω| = 0.30 m, angle |ω·t| = π/4 rad, arc length ≈ 0.235619 m, speed and duration bounds, total time, and net heading change of zero. My order test checked the sign sequence [+, −, +, −], equal angular magnitudes, equal forward speed of 0.21 m/s, and no zero/zero stop segment. Together, they show the path is ordered correctly, each arc has the required radius and angle, the robot finishes facing its initial direction, and the stop is not duplicated.

These tests do not establish real-world repeatability. They do not show that wheel slip, latency, acceleration limits, floor friction, or calibration will keep every real run within the course tolerances of 0.02 m radius, 0.04 rad angle, and 0.02 m distance. The Live motion and stop pass is one run, not many. They also do not verify a full 1 s final hold, because build_pattern intentionally omits a stop segment and relies on the wrapper.

One additional test I would need is a repeated real-robot or high-fidelity simulation run with odometry logging: after each segment, compute best-fit radius, turn angle, and arc length; after the fourth, verify final heading and position; and confirm zero velocity is commanded for at least 1 s. Repeat several times to check drift and tolerance margins.

## Live Pending

False

## Modifications

I added the pattern-name guard: if pattern_name != "alternating_arcs": raise ValueError(...) to satisfy the requirement to reject unknown names, rather than silently returning an empty list or the wrong pattern. I chose omega = 0.70 rad/s and derived v = radius * omega = 0.21 m/s instead of hard-coding v = 0.21, so that the radius relationship R = |v/ω| stays exact. I derived duration = (π/4) / 0.70 ≈ 1.121997 s from t = |Δθ/ω| rather than typing the decimal, so the duration follows directly from the stated relationship. I did not add a final zero-velocity segment because the wrapper publishes the stop and the evaluator verifies it, and adding one here would double-count the stop.

## Original Output

Assumptions: Segment is already defined in pattern.py with fields linear_x, angular_z, and duration. The wrapper repeatedly publishes each returned segment for its duration, then sends zero velocity. I will not modify the wrapper or the course checks.

Geometry: Radius R = 0.30 m. Angular speed magnitude |ω| = 0.70 rad/s. Linear speed v = R|ω| = 0.30 × 0.70 = 0.21 m/s, which is within 0.22 m/s. Each turn angle is π/4 rad, so each segment duration is (π/4)/0.70 ≈ 1.121997 s. Four segments give total duration ≈ 4.48799 s, within 60 s. Each segment is within 30 s.

The four segments are: forward left +45°, forward right -45°, forward left +45°, forward right -45°. Because the angular speeds are equal and opposite in pairs, the net heading change is zero, so the final heading equals the initial heading.

Unknown pattern names raise ValueError. The returned list contains exactly four Segment objects in the required order. No intermediate zero-velocity stop is inserted because the wrapper only sends zero at the end; the sign change between segments is handled by the next segment’s angular_z.

Proposed tests: check len(segments) == 4; check each duration > 0 and ≤ 30; check total duration ≤ 60; check abs(segment.linear_x) ≤ 0.22; check abs(segment.angular_z) ≤ 0.80; check linear_x == 0.21 for all; check angular_z sequence is [+0.70, -0.70, +0.70, -0.70]; check radius = linear_x / abs(angular_z) = 0.30 for all; check total heading change sums to 0; check unknown pattern raises ValueError.

## Original Prompt

This is a ROS 2 Jazzy Python package. Implement only build_pattern(pattern_name: str) -> list[Segment] for 'alternating_arcs' in the existing pattern.py.
The course-provided pattern_node.py calls this function, publishes the returned segments repeatedly through /student_cmd_vel, and sends the final zero command.
Use the existing Segment class with linear_x (m/s), angular_z (rad/s), and duration (s).
Return the ordered segments for the assigned specification and raise ValueError for an unknown pattern name.
Stay within 0.22 m/s, 0.80 rad/s, 30 seconds per segment, and 60 seconds total.
Do not replace the wrapper or course checks. Explain assumptions and propose tests.

Specification:
Start at (0.50, 0.50, 0) m/rad, at rest, in a clear 2 m by 2 m area. Robot body frame: +x forward, +y left; positive angular velocity turns left. Drive four forward circular arcs of radius 0.30 m: +45°, -45°, +45°, -45°. Finish facing the initial direction. Use angular speed ±0.70 rad/s and linear speed 0.21 m/s. Each arc duration = (pi/4)/0.70 ≈ 1.121997 s. Total ≈ 4.488 s. Execute arcs back-to-back, switching angular velocity sign at boundaries; after the fourth arc, command zero and hold. Limits: |v|≤0.22 m/s, |ω|≤0.80 rad/s, each segment ≤30 s, total ≤60 s. Success: each arc radius within 0.02 m of 0.30 m, each turn within 0.04 rad of 45°, each arc distance within 0.02 m of 0.235619 m, final heading within 0.04 rad of the initial heading, live checkpoints within 0.15 m and 0.20 rad.

## Original Source

import math

def build_pattern(pattern_name: str) -> list[Segment]:
if pattern_name != "alternating_arcs":
raise ValueError(f"Unknown pattern name: {pattern_name!r}")

radius = 0.30
angular_speed = 0.70
linear_speed = radius * angular_speed
arc_angle = math.pi / 4.0
duration = arc_angle / angular_speed

return [
Segment(linear_x=linear_speed, angular_z=angular_speed, duration=duration),
Segment(linear_x=linear_speed, angular_z=-angular_speed, duration=duration),
Segment(linear_x=linear_speed, angular_z=angular_speed, duration=duration),
Segment(linear_x=linear_speed, angular_z=-angular_speed, duration=duration),
]

## Problems

One omission is that the generated code does not include an explicit final hold segment. The specification says to hold the final pose briefly, at least 1 s, but the code relies on the wrapper’s final zero command. If the wrapper does not hold zero for at least 1 s, we need to add a final Segment(linear_x=0.0, angular_z=0.0, duration=1.0). 
I also checked the code to ensure that Segment must be in scope, or the code raises a NameError. The sign convention for angular_z is assumed rather than verified.
The numerical values are correct: |v| = 0.21 ≤ 0.22, |ω| = 0.70 ≤ 0.80, each duration 1.121997 ≤ 30, and total 4.48799 ≤ 60.

## Saved Specification

Robot body frame is +x forward, +y left. Heading θ is measured from world +x; positive angular velocity means turning left/CCW. 

All arcs are driven forward, so linear speed is positive along body +x. Initial pose: Start at (x,y,θ)=(0.50,0.50,0)m, rad inside a 2m×2m area, facing +x. 
Intended sequence: The robot drives four forward circular arcs, each with radius R = 0.30 m.

+45°, −45°, +45°, −45°, so the robot finishes facing the initial direction; use |ω|=0.70 rad/s and 
v=R|ω|=0.21 m/s, giving each arc duration (π/4)/0.70≈1.122 s and total time≈4.488 s, all within the 0.22 m/s, 0.80 rad/s, 30 s per segment, and 60 s total limits. The robot runs  these arcs back-to-back without full stops by switching the sign of angular velocity at each boundary; after the fourth arc, command v=0 and ω=0 and hold the final pose briefly

Measurable success criteria are: each measured arc radius within 0.02 m of 0.30 m, each turn within 0.04 rad of 45°, each intended arc distance within 0.02 m of 0.235619 m, final heading within 0.04 rad of the initial heading, final relative displacement within course tolerance of (0.848528, 0.351472) m, live checkpoints within 0.15 m and 0.20 rad, and all speeds and durations within the stated limits.

## Specification

Robot body frame is +x forward, +y left. Heading θ is measured from world +x; positive angular velocity means turning left/CCW. 

All arcs are driven forward, so linear speed is positive along body +x. Initial pose: Start at (x,y,θ)=(0.50,0.50,0)m, rad inside a 2m×2m area, facing +x. 
Intended sequence: The robot drives four forward circular arcs, each with radius R = 0.30 m.

+45°, −45°, +45°, −45°, so the robot finishes facing the initial direction; use |ω|=0.70 rad/s and 
v=R|ω|=0.21 m/s, giving each arc duration (π/4)/0.70≈1.122 s and total time≈4.488 s, all within the 0.22 m/s, 0.80 rad/s, 30 s per segment, and 60 s total limits. The robot runs  these arcs back-to-back without full stops by switching the sign of angular velocity at each boundary; after the fourth arc, command v=0 and ω=0 and hold the final pose briefly

Measurable success criteria are: each measured arc radius within 0.02 m of 0.30 m, each turn within 0.04 rad of 45°, each intended arc distance within 0.02 m of 0.235619 m, final heading within 0.04 rad of the initial heading, final relative displacement within course tolerance of (0.848528, 0.351472) m, live checkpoints within 0.15 m and 0.20 rad, and all speeds and durations within the stated limits.

## Test Plan

Before running, a pattern behavior test should call build_pattern("alternating_arcs") and expect exactly four segments, all with linear_x = 0.21, an angular_z sequence [+0.70, −0.70, +0.70, −0.70], each duration of about 1.121997 s, each radius of 0.30 m, and a net heading change of zero. Expected result: pass. 

A velocity-limit test should assert every abs(linear_x) ≤ 0.22, every abs(angular_z) ≤ 0.80, every duration > 0 and ≤ 30, and total duration ≤ 60. Expected result: pass with values 0.21, 0.70, 1.121997, and 4.48799. 

A stop test should verify that after the fourth segment, the wrapper publishes zero velocity, with expected final command linear_x = 0.0 and angular_z = 0.0. If a 1 s hold is required, the current generated code alone does not provide it, so the test should confirm that the wrapper holds zero velocity, or the code should add the final zero-velocity segment.
