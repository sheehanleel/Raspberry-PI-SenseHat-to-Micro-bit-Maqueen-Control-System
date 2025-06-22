import time


#Pi sends commands (writes to a file)
# Simulated Pi controller
class PiController:
    def __init__(self, robot):
        self.robot = robot

    def send_command(self, cmd):
        print(f"[Pi] Sending command: {cmd}")
        self.robot.receive_command(cmd)
        time.sleep(1)