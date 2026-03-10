import cv2 
import rclpy 
from rclpy.node import Node 

from sensor_msgs.msg import Image
from cv_bridge import CvBridge 

class CameraPublisher(Node):
    def __init__(self):
        super().__init__("camera_publisher")
        
        self.publisher_ =self.create_publisher(Image, '/camera/image_raw', 10)
        
        self.bridge = CvBridge()
        
        self.cap = cv2.VideoCapture(0)
        
        self.timer = self.create_timer(1.0/ 30.0, self.timer_callback)
        
    def timer_callback(self):
        
        ret, frame = self.cap.read()
        
        if ret:
            msg = self.bridge.cv2_to_imgmsg(frame, encoding='bgr8')
            msg.header.stamp = self.get_clock().now().to_msg()
            msg.header.frame_id = 'camera_frame'
            
            self.publisher_.publish(msg)
            
def main():
    rclpy.init()
    node = CameraPublisher()
    rclpy.spin(node)
    node.destroy_node()
    recly.shutdown()
