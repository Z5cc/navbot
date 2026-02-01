import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.actions import SetEnvironmentVariable, IncludeLaunchDescription
from launch.conditions import IfCondition
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration, PathJoinSubstitution
from launch_ros.substitutions import FindPackageShare
from launch_ros.actions import Node, LifecycleNode, SetParameter


def generate_launch_description():
    pkg_navbot = get_package_share_directory('navbot')
    slam_params_file=PathJoinSubstitution([pkg_navbot, 'config', 'slam.yaml'])
    use_sim_time = SetParameter(name='use_sim_time', value=True)

    # talker = Node(
    #     package='demo_nodes_cpp',
    #     executable='talker',
    #     name='talker'
    # )

    # listener = Node(
    #     package='demo_nodes_cpp',
    #     executable='listener',
    #     name='listener'
    # )

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

    lidar_transform = Node(
        package='tf2_ros',
        executable='static_transform_publisher',
        arguments=[
            '--x', '0.43', '--y', '0', '--z', '0.26',
            '--yaw', '0', '--pitch', '0', '--roll', '0',
            '--frame-id', 'X1/base_link', '--child-frame-id', 'X1/base_link/gpu_lidar']
    )

    slam = Node(
        package='slam_toolbox',
        executable='async_slam_toolbox_node',
        name='slam',
        parameters=[slam_params_file, {'use_sim_time': 'false'}],
    )


    return LaunchDescription([
        use_sim_time,
        # listener,
        # talker
        # map_server,
        lidar_transform,
        slam
    ])
