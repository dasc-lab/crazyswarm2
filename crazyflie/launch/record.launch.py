import launch
from datetime import datetime

def generate_launch_description():

    now = datetime.now() # current date and time
    timestamp = now.strftime("%Y-%m-%d_%H-%M-%S")

    bagname = f"run7_{timestamp}"

    topics = [
            "/tf",
            "/poses",
            "/cf1/topic_name1",
            "/cf1/topic_name3",
            "/cf1/cmd_position",
            "/cf1/cmd_full_state",
            "/cf1/cmd_vel_legacy",
            ]

    return launch.LaunchDescription([
        launch.actions.ExecuteProcess(
            cmd=['ros2', 'bag', 'record'] + topics + ["-o", bagname],
            cwd=["/root/colcon_ws/bags"],
            output='screen'
        )
    ])
                 
