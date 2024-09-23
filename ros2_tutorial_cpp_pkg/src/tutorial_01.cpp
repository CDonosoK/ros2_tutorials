#include "rclcpp/rclcpp.hpp"

class SimplePublisher: public rclcpp ::Node{
    public:
        SimplePublisher(): Node("my_node_cpp"), counter_(0){
            timer_ = this -> create_wall_timer(
                std::chrono::seconds(1), // Se le agrega el rate
                std::bind(&SimplePublisher::timerCallback, this) // Se hace un bind para poder utilizar la funcion de la clase
            );
        }

    private:

    void timerCallback(){ // Funcion callback para llamar
        counter_ ++;
        RCLCPP_INFO(this -> get_logger(), "Hello cpp - %d", counter_);
        
    }

    // Variables utilizadas
    rclcpp::TimerBase::SharedPtr  timer_;
    int counter_;

};


int main(int argc, char **argv){
    
    rclcpp::init(argc, argv); // Se inicializa el nodo

    auto node = std::make_shared<SimplePublisher>();

    rclcpp::spin(node); // Se hace un spin para mantener vivo el nodo
    
    rclcpp::shutdown(); // Se terminal el nodo

    return 0;
}