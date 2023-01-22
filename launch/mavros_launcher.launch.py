
from launch import LaunchDescription
import launch.substitutions
import launch_ros.actions

def generate_launch_description():
    my_config_file = launch.substitutions.LaunchConfiguration(
        'my_config', default=[launch.substitutions.ThisLaunchFileDir(), '/config/px4/mavros_params.yaml']
    )

    # px4_config_file = launch.substitutions.LaunchConfiguration(
    #     'px4_config', default=[launch.substitutions.ThisLaunchFileDir(), '/config/px4/px4_config.yaml']
    # )

    mavros_time_config_file = launch.substitutions.LaunchConfiguration(
        'mavros_time_config', default=[launch.substitutions.ThisLaunchFileDir(), '/config/px4/mavros_time.yaml']
    )

    mavros_cmd_config_file = launch.substitutions.LaunchConfiguration(
        'mavros_cmd_config', default=[launch.substitutions.ThisLaunchFileDir(), '/config/px4/mavros_cmd.yaml']
    )
    
    mavros_global_position_config_file = launch.substitutions.LaunchConfiguration(
        'mavros_global_position_config', default=[launch.substitutions.ThisLaunchFileDir(), '/config/px4/mavros_global_position.yaml']
    )

    mavros_imu_config_file = launch.substitutions.LaunchConfiguration(
        'mavros_imu_config', default=[launch.substitutions.ThisLaunchFileDir(), '/config/px4/mavros_imu.yaml']
    )

    mavros_local_position_config_file = launch.substitutions.LaunchConfiguration(
        'mavros_local_position_config', default=[launch.substitutions.ThisLaunchFileDir(), '/config/px4/mavros_local_position.yaml']
    )

    mavros_mission_config_file = launch.substitutions.LaunchConfiguration(
        'mavros_mission_config', default=[launch.substitutions.ThisLaunchFileDir(), '/config/px4/mavros_mission.yaml']
    )
    mavros_params_config_file = launch.substitutions.LaunchConfiguration(
        'mavros_params_config', default=[launch.substitutions.ThisLaunchFileDir(), '/config/px4/mavros_params.yaml']
    )
    mavros_setpoint_accel_config_file = launch.substitutions.LaunchConfiguration(
        'mavros_setpoint_accel_config', default=[launch.substitutions.ThisLaunchFileDir(), '/config/px4/mavros_setpoint_accel.yaml']
    )

    mavros_setpoint_attitude_config_file = launch.substitutions.LaunchConfiguration(
        'mavros_setpoint_attitude_config', default=[launch.substitutions.ThisLaunchFileDir(), '/config/px4/mavros_setpoint_attitude.yaml']
    )

    mavros_setpoint_position_config_file = launch.substitutions.LaunchConfiguration(
        'mavros_setpoint_position_config', default=[launch.substitutions.ThisLaunchFileDir(), '/config/px4/mavros_setpoint_position.yaml']
    )
    mavros_setpoint_raw_config_file = launch.substitutions.LaunchConfiguration(
        'mavros_setpoint_raw_config', default=[launch.substitutions.ThisLaunchFileDir(), '/config/px4/mavros_setpoint_raw.yaml']
    )
    mavros_setpoint_velocity_config_file = launch.substitutions.LaunchConfiguration(
        'mavros_setpoint_velocity_config', default=[launch.substitutions.ThisLaunchFileDir(), '/config/px4/mavros_setpoint_velocity.yaml']
    )
    mavros_sys_config_file = launch.substitutions.LaunchConfiguration(
        'mavros_sys_config', default=[launch.substitutions.ThisLaunchFileDir(), '/config/px4/mavros_time.yaml']
    )

    return LaunchDescription([
        launch_ros.actions.Node(
            package='mavros',
            executable='mavros_node',
            output='screen',
            parameters=[
                my_config_file,
                mavros_time_config_file,
                mavros_cmd_config_file,
                mavros_global_position_config_file,
                mavros_imu_config_file,
                mavros_local_position_config_file,
                mavros_mission_config_file,
                mavros_params_config_file,
                mavros_setpoint_accel_config_file,
                mavros_setpoint_attitude_config_file,
                mavros_setpoint_position_config_file,
                mavros_setpoint_raw_config_file,
                mavros_setpoint_velocity_config_file,
                mavros_sys_config_file
            ]
        )
    ])