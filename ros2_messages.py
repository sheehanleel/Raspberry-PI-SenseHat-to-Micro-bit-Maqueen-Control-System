# Simulated geometry_msgs/Twist message
class Twist:
    def __init__(self, linear_x=0, angular_z=0): #From the input_node getting linear and angular value to be sent to comm_node
        self.linear = {"x": linear_x}
        self.angular = {"z": angular_z}