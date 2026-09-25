import os
import unittest
from week03_pattern.pattern import build_pattern


class MyPatternTests(unittest.TestCase):
    def test_my_pattern_geometry(self):
        segments = build_pattern(os.environ["WEEK03_ASSIGNED_PATTERN"])
        # Alternating arcs: four 45-degree arcs of radius 0.30 m.
        self.assertEqual(len(segments), 4)
        self.assertAlmostEqual(0.30, 0.21 / 0.70, places=6)
        for segment in segments:
            # Forward motion only.
            self.assertGreater(segment.linear_x, 0.0)
            # Radius R = |v / omega| must be 0.30 m.
            self.assertAlmostEqual(0.30, abs(segment.linear_x / segment.angular_z), places=6)
            # Arc angle |omega * t| must be 45 degrees = pi/4 rad.
            self.assertAlmostEqual(3.141592653589793 / 4.0, abs(segment.angular_z * segment.duration), places=6)
            # Arc length v * t must be R * angle = 0.30 * pi/4 = 0.235619 m.
            self.assertAlmostEqual(0.235619, segment.linear_x * segment.duration, places=5)
            # Speed limits.
            self.assertLessEqual(abs(segment.linear_x), 0.22)
            self.assertLessEqual(abs(segment.angular_z), 0.80)
            self.assertGreater(segment.duration, 0.0)
            self.assertLessEqual(segment.duration, 30.0)
        # Total time within 60 s.
        self.assertLessEqual(sum(s.duration for s in segments), 60.0)
        # Net heading change must be zero: finishes facing initial direction.
        net_heading = sum(s.angular_z * s.duration for s in segments)
        self.assertAlmostEqual(0.0, net_heading, places=6)

    def test_my_pattern_order(self):
        segments = build_pattern(os.environ["WEEK03_ASSIGNED_PATTERN"])
        # Sign sequence must be +, -, +, - for +45, -45, +45, -45.
        signs = [1 if s.angular_z > 0 else -1 for s in segments]
        self.assertEqual([1, -1, 1, -1], signs)
        # Magnitudes must all match so the pairs cancel.
        magnitudes = [abs(s.angular_z) for s in segments]
        for magnitude in magnitudes:
            self.assertAlmostEqual(magnitudes[0], magnitude, places=6)
        # Each segment moves forward with the same linear speed.
        for segment in segments:
            self.assertAlmostEqual(0.21, segment.linear_x, places=6)
        # No segment in the returned list is a stop command; the wrapper owns the stop.
        for segment in segments:
            self.assertFalse(segment.linear_x == 0.0 and segment.angular_z == 0.0)


if __name__ == "__main__":
    unittest.main()