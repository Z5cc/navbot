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

    talker = Node(
            package='demo_nodes_cpp',
            executable='talker',
            name='talker'
    )

    listener = Node(
        package='demo_nodes_cpp',
        executable='listener',
        name='listener'
    )

    # map_server = Node(
    #     package='nav2_map_server',
    #     executable='map_server',
    #     output='screen',
    #     parameters=[{'yaml_filename': map_file_path}]
    # )

    # start_lifecycle_manager = Node(
    #     package='nav2_lifecycle_manager',
    #     executable='lifecycle_manager',
    #     name='lifecycle_manager',
    #     output='screen',
    #     emulate_tty=True,
    #     parameters=[{'use_sim_time': True},r
    #                 {'autostart': True},
    #                 {'node_names': ['map_server']}]
    # )

    return LaunchDescription([
        listener,
        talker
        # map_server,
    ])
