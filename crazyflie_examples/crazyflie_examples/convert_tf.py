import rclpy
from rclpy.node import Node

from tf2_ros import TransformException
from tf2_ros.buffer import Buffer
from tf2_ros.transform_listener import TransformListener
from geometry_msgs.msg import Vector3

class FramePublisher(Node):
	def __init__(self):
		super().__init__('life_is_hard')
		self.tf_buffer = Buffer()
		self.tf_listener = TransformListener(self.tf_buffer, self)
		


if __name__ == '__main__':
	
	pass
