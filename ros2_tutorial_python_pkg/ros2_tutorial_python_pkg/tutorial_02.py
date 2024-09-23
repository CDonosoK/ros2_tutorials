import rclpy
from rclpy.node import Node
from example_interfaces.msg import String
    
    
class SimplePublisher(Node):
    def __init__(self):
        super().__init__("simple_publisher")

        self.publisher = self.create_publisher(String, 'simple_publisher', 10)
        self.create_timer(0.5, self.publish_message)
        self.get_logger().info('Simple publisher node has been started')

    def publish_message(self):
        msg = String()
        msg.data = 'Hello from node simple_publisher'
        self.publisher.publish(msg)
    
    
def main(args=None):
    rclpy.init(args=args)
    node = SimplePublisher()
    rclpy.spin(node)
    rclpy.shutdown()
    
    
if __name__ == "__main__":
    main()