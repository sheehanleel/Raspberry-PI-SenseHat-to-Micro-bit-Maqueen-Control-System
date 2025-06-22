import time

# Simulated micro:bit/Maqueen robot class
class VirtualMaqueen:
    def receive_command(self, cmd):
        actions = {
            'FWD': 'Moving Forward',
            'STOP': 'Stopping',
            'LEFT': 'Turning Left',
            'RIGHT': 'Turning Right'
        }
        print(f"[Maqueen] {actions.get(cmd, 'Unknown Command')}")