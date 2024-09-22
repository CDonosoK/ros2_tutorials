cmake_minimum_required(VERSION 3.8)
project(ros2_tutorial_cpp_pkg)

# Default to C++ 14
if (NOT CMAKE_CXX_STANDARD)
  set(CMAKE_CXX_STANDARD 14)
endif()

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# find dependencies
find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)

# Nombre_del_nodo Ubicacion_del_archivo
add_executable(tutorial_00_cpp_node src/tutorial_00/my_first_node.cpp)
ament_target_dependencies(tutorial_00_cpp_node rclcpp)

install(
  TARGETS
  tutorial_00_cpp_node
  DESTINATION lib/${PROJECT_NAME}
)

ament_package()
