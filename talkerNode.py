#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class MyNode(Node):
    def __init__(bolo):
        super().__init__('talker')
        bolo.publisher = bolo.create_publisher(String, "chatter", 10)
        bolo.timer = bolo.create_timer(1.0, bolo.timer_callback)
        bolo.counter = 0
    def timer_callback(send):
        msg = String()
        msg.data = 'hi: %d' % send.counter
        send.publisher.publish(msg)
        send.get_logger().info('Out: "%s"' % msg.data)
        send.counter += 1

def main(args=None):
    rclpy.init(args=args)
    node = MyNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()