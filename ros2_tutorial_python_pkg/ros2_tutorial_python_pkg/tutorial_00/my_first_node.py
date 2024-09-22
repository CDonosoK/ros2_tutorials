import rclpy
from rclpy.node import Node

class SimplePublisherNode(Node): #Instanciamos la clase para que herede
    def __init__(self):
        super().__init__("simple_publisher") # Nombre del nodo
        self.get_logger().info("Simple publisher initialize")
        self.counter_ = 0
        self.rate = 10 # Cuantos iteraciones por segundo
        self.rate = 1/self.rate #Se realiza la conversión a Hz

        self.create_timer(self.rate, self.timer_callback) #Se le da el rate y la función a ejecutar con ese rate

    def timer_callback(self):
        self.get_logger().info("Hello py - " + str(self.counter_))
        self.counter_ += 1

def main(args=None):
    rclpy.init(args = args) #Se inicializan los elementos de ROS2

    node = SimplePublisherNode()
    
    rclpy.spin(node) #Spin funciona de la misma manera
    rclpy.shutdown() #El nodo se termina

if __name__ == "__main__":
    main()