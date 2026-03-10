#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from unitree_api.msg import Request
from std_msgs.msg import Header
from geometry_msgs.msg import Twist

class SportRequestPublisher(Node):
    def __init__(self):
        super().__init__('sport_request_publisher')
        self.publisher = self.create_publisher(Request, '/api/sport/request', 10)
        self.timer = self.create_timer(0.01, self.timer_callback)
        self.cmd_vel_subscriber = self.create_subscription(Twist, '/cmd_vel', self.cmd_vel_callback, 10)
        self.cmd_vel_flag = False
        self.linear_x = None
        self.linear_y = None
        self.angular_z = None


    def timer_callback(self):
        request_msg = Request()
        if self.cmd_vel_flag == True:
            # Set identity information
            request_msg.header.identity.api_id = 1008

            # Set lease information
            request_msg.header.lease.id = 0

            # Set policy information
            request_msg.header.policy.priority = 0
            request_msg.header.policy.noreply = True

            # Set parameter information
            request_msg.parameter = f'{{"x":{self.linear_x},"y":{self.linear_y},"z":{self.angular_z}}}'

            # Set binary information (empty in this example)
            request_msg.binary = []

            if self.linear_x == 0 and self.linear_y == 0 and self.angular_z == 0:
                request_msg.header.identity.api_id = 1034    
                        
        else :
            request_msg.header.identity.api_id = 1034

        self.publisher.publish(request_msg)
        #self.get_logger().info('Request message published')
        self.cmd_vel_flag = False
        
    def cmd_vel_callback(self, msg):
        if msg != None:
            self.cmd_vel_flag = True
            self.cmd_vel = msg

            # Update linear and angular velocities from cmd_vel message
            self.linear_x = msg.linear.x
            self.linear_y = msg.linear.y
            self.angular_z = msg.angular.z

def main(args=None):
    rclpy.init(args=args)
    sport_request_publisher = SportRequestPublisher()
    rclpy.spin(sport_request_publisher)
    sport_request_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
