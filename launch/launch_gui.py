import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.actions import SetEnvironmentVariable, IncludeLaunchDescription
from launch.conditions import IfCondition
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration, PathJoinSubstitution
from launch_ros.substitutions import FindPackageShare
from launch_ros.actions import Node, LifecycleNode


def generate_launch_description():
    pkg_navbot = get_package_share_directory('navbot')
    world_file_path = PathJoinSubstitution([pkg_navbot, 'worlds', 'world.sdf'])
    assets_folder = PathJoinSubstitution([pkg_navbot, 'worlds', 'assets'])
    rviz_file_path = PathJoinSubstitution([pkg_navbot, 'rviz', 'rviz.rviz'])
    # map_file_path = os.path.join(pkg_navbot,'maps','willow.yaml')

    pkg_ros_gz_sim = get_package_share_directory('ros_gz_sim')
    launch_file_path = PathJoinSubstitution([pkg_ros_gz_sim, 'launch', 'gz_sim.launch.py'])

    gz_env_var = SetEnvironmentVariable(name='GZ_SIM_RESOURCE_PATH', value=assets_folder)

    gz_sim = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(launch_file_path),
        launch_arguments={'gz_args': [world_file_path]}.items(),
    )

    rviz = Node(
            package='rviz2',
            namespace='rviz2',
            executable='rviz2',
            name='rviz2',
            arguments=['-d', rviz_file_path]
    )

    return LaunchDescription([
        gz_env_var,
        gz_sim,
        rviz,
    ])
