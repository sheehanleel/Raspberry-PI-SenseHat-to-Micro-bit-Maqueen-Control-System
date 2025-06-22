# Communication Node subscribes to 'Twist', converts to Maqueen command

class CommNode:
    def __init__(self, robot):
        self.robot = robot

    def handle_twist(self, twist):
        if twist.linear["x"] > 0:
            cmd = "FWD"
        elif twist.linear["x"] < 0:
            cmd = "REV"
        elif twist.angular["z"] > 0:
            cmd = "LEFT"
        elif twist.angular["z"] < 0:
            cmd = "RIGHT"
        else:
            cmd = "STOP"
        print(f"[CommNode] Converted Twist to command: {cmd}")
        self.robot.receive_command(cmd) #Sends the received linear(x) and angular(z) values to the mock Maqueen robot.