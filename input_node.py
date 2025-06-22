from sense_hat import SenseHat
from ros2_messages import Twist

# This would publish messages to a topic in ROS2
class InputNode:
    def __init__(self, events):
        self.sensehat = SenseHat(events=events)

    def get_next_twist(self):
        # Simulate mapping joystick to Twist message
        mapping = {
            "up": Twist(linear_x=1),
            "down": Twist(linear_x=-1),
            "left": Twist(angular_z=1),
            "right": Twist(angular_z=-1),
            "middle": Twist(linear_x=0, angular_z=0)
        }
        for event in self.sensehat.stick.get_events():
            yield mapping.get(event["direction"], Twist()) #gets the direction from main.py "custom_events"