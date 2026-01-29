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
from ros_gz_bridge.actions import RosGzBridge


def generate_launch_description():
    pkg_navbot = get_package_share_directory('navbot')
    world_file_path = PathJoinSubstitution([pkg_navbot, 'worlds', 'world.world'])
    assets_folder = PathJoinSubstitution([pkg_navbot, 'worlds', 'assets'])
    plugin_folder = PathJoinSubstitution([pkg_navbot, 'plugins'])
    rviz_config_path = PathJoinSubstitution([pkg_navbot, 'config', 'rviz.rviz'])
    ros_gz_bridge_config_path = PathJoinSubstitution([pkg_navbot, 'config', 'ros_gz_bridge.yaml'])
    # map_file_path = os.path.join(pkg_navbot,'maps','willow.yaml')

    pkg_ros_gz_sim = get_package_share_directory('ros_gz_sim')
    launch_file_path = PathJoinSubstitution([pkg_ros_gz_sim, 'launch', 'gz_sim.launch.py'])

    gz_resource_var = SetEnvironmentVariable('GZ_SIM_RESOURCE_PATH', assets_folder)
    gz_plugin_var = SetEnvironmentVariable('GZ_SIM_PLUGIN_PATH', plugin_folder)
    
    use_sim_time = SetParameter(name='use_sim_time', value=True)

    gz_sim = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(launch_file_path),
        launch_arguments={'gz_args': ['-r ', world_file_path]}.items(),
    )
    ros_gz_bridge = RosGzBridge(
        bridge_name='bridge_node',
        config_file=ros_gz_bridge_config_path,
    )

    rviz = Node(
        package='rviz2',
        namespace='rviz2',
        executable='rviz2',
        name='rviz2',
        arguments=['-d', rviz_config_path]
    )


    return LaunchDescription([
        use_sim_time,
        gz_resource_var,
        gz_plugin_var,
        gz_sim,
        ros_gz_bridge,
        rviz,
    ])
