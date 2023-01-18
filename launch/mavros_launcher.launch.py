
from launch import LaunchDescription
import launch.substitutions
import launch_ros.actions

def generate_launch_description():
    my_config_file = launch.substitutions.LaunchConfiguration(
        'my_config', default=[launch.substitutions.ThisLaunchFileDir(), '/config/mavros_params.yaml']
    )

    px4_config_file = launch.substitutions.LaunchConfiguration(
        'px4_config', default=[launch.substitutions.ThisLaunchFileDir(), '/config/mavros_params.yaml']
    )

    return LaunchDescription([
        launch_ros.actions.Node(
            package='mavros',
            executable='mavros_node',
            output='screen',
            parameters=[my_config_file]
        )
    ])