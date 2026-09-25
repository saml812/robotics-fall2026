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