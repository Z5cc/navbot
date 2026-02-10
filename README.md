# SLAM-Based Autonomous Navigation for UGVs

2026-02-10 by David Nicklaser

## Installation

Install Ubuntu 24.04 LTS.

Install ROS jazzy according to https://docs.ros.org/en/jazzy/Installation/Ubuntu-Install-Debs.html

Install colcon and the following ROS packages:
```bash
sudo apt install python3-colcon-common-extensions
sudo apt install ros-jazzy-ros-gz
sudo apt install ros-jazzy-navigation2
sudo apt install ros-jazzy-nav2-map-server
sudo apt install ros-jazzy-nav2-bringup
sudo apt install ros-jazzy-slam-toolbox
```

Create a ROS2 workspace and clone the repo into *src*:
```bash
mkdir -p ros2_ws/src
cd ros2_ws/src
git clone https://github.com/Z5cc/navbot.git
```

Move into the *ros2_ws* folder and build the project with colcon:
```bash
cd ..
colcon build --symlink-install  --cmake-args -DCMAKE_BUILD_TYPE=RelWithDebInfo
```

## Debugging

Stay in the *ros2_ws* folder and open this folder as a project via VSCode:
```bash
code .
```

Copy the launch config files from *vscode_backup* to *.vscode*:
```bash
cp src/navbot/vscode/* .vscode 
```

Under 'Rund and Debug' select 'launch' as the launch config and press the green arrow 'Start Debugging'.

## Demo

Stay in the *ros2_ws* folder and source the ros2 underlay and overlay:
```bash
source /opt/ros/jazzy/setup.bash
source install/local_setup.bash
```

Run the launch files:
```bash
ros2 launch navbot launch_sim.py
ros2 launch navbot launch_nodes.py
```

Run the keyboard node:
```bash
ros2 run teleop_twist_keyboard teleop_twist_keyboard
```

Use the keys as instructed to navigate the robot. The map built will be visualized in RVIZ. The following GIF shows the complete setup with RVIZ on the left side and the Gazebo simulation on the right side.

![gif](demo.gif)
