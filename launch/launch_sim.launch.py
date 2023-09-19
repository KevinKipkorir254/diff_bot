import os

from ament_index_python.packages import get_package_share_directory


from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource

from launch_ros.actions import Node



def generate_launch_description():


    # Include the robot_state_publisher launch file, provided by our own package. Force sim time to be enabled
    # !!! MAKE SURE YOU SET THE PACKAGE NAME CORRECTLY !!!

    package_name='diff_bot' #<--- CHANGE ME

    rsp = IncludeLaunchDescription(
                PythonLaunchDescriptionSource([os.path.join(
                    get_package_share_directory(package_name),'launch','rsp.launch.py'
                )]), launch_arguments={'use_sim_time': 'true'}.items()
    )

    # Include the Gazebo launch file, provided by the gazebo_ros package this launches gazebo
    gazebo = IncludeLaunchDescription(
                PythonLaunchDescriptionSource([os.path.join(
                    get_package_share_directory('gazebo_ros'), 'launch', 'gazebo.launch.py')]),
             )

    # This causes the robot to appear
    spawn_entity = Node(package='gazebo_ros', executable='spawn_entity.py',
                        arguments=['-topic', 'robot_description',
                                   '-entity', 'diff_bot'],
                        output='screen')
    
    # This causes the robot to appear
    publisher_ = Node(package='joint_state_publisher', executable='joint_state_publisher')
    # This causes the robot to appear
    gui = Node(package='joint_state_publisher_gui', executable='joint_state_publisher_gui')
    # This causes the robot to appear
    rviz = Node(package='rviz2', executable='rviz2')



    # Launch them all!
    return LaunchDescription([
        rsp,
        gazebo,
        spawn_entity,
        publisher_,
        gui,
        rviz,

    ])