# 1. GO2 Package Install 
## 1.1. Git 
    ```bash
    git clone https://github.com/unitreerobotics/unitree_ros2
    ```
    
## 1.2. Dependencies Install
    ```bash
    sudo apt install ros-humble-rmw-cyclonedds-cpp
    sudo apt install ros-humble-rosidl-generator-dds-idl
    sudo apt install libyaml-cpp-dev
    ```
    
## 1.3. Package Build
    ```bash
    cd unitree_ros2/cyclonedds_ws/
    source /opt/ros/humble/setup.bash
    colcon build
    ```
