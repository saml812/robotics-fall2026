"""Mission 2 student implementation.

Complete only ``transform_camera_point`` after preserving the initial AI output
in the guide. Course tests supply both real and simulated TF buffers.
"""
import tf2_ros
import tf2_geometry_msgs  # noqa: F401  # registers PointStamped with tf2
from geometry_msgs.msg import PointStamped
from rclpy.duration import Duration
from rclpy.time import Time


def transform_camera_point(tf_buffer, point: PointStamped) -> PointStamped | None:
    """Return a hall_camera point expressed in base_link, or None if unavailable."""
    if point.header.frame_id != "hall_camera":
        raise ValueError(
            f"Expected point.header.frame_id 'hall_camera', got {point.header.frame_id!r}"
        )

    try:
        return tf_buffer.transform(
            point, "base_link", timeout=Duration(seconds=0.5)
        )
    except tf2_ros.TransformException:
        pass

    latest = PointStamped()
    latest.header.frame_id = point.header.frame_id
    latest.header.stamp = Time()  # zero time == latest available in tf2
    latest.point = point.point

    try:
        return tf_buffer.transform(
            latest, "base_link", timeout=Duration(seconds=0.5)
        )
    except tf2_ros.TransformException:
        return None