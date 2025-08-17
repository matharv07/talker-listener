#!/usr/bin/env python3
"""
import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class MyNode(Node):
    def __init__(sunlo):
        super().__init__('listener')
        sunlo.subscription = sunlo.create_subscription(String, 'chatter', sunlo.listener_callback, 10)
        sunlo.subscription
        sunlo.get_logger().info("hihi")

    def listener_callback(recieve, message):
        recieve.get_logger().info("talker sent:", message.data)

def main(args=None):
    rclpy.init(args=args)
    node = MyNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
"""

import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class MyNode(Node):
    def __init__(sunlo):
        super().__init__('listener')
        sunlo.subscription = sunlo.create_subscription(String, 'chatter', sunlo.listener_callback, 10)
        sunlo.subscription
    def listener_callback(recieve, msg):
        recieve.get_logger().info('Talker sent: ' + msg.data)


def main(args=None):
    rclpy.init(args=args)
    node = MyNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()