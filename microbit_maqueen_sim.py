import time

# Simulated micro:bit/Maqueen robot class
class VirtualMaqueen:
    def receive_command(self, cmd):
        actions = {
            'FWD': 'Moving Forward',
            'LEFT': 'Turning Left',
            'REV': 'Moving Backwards',
            'RIGHT': 'Turning Right',
            'STOP': 'Stopping'
        }
        print(f"[Maqueen] {actions.get(cmd, 'Unknown Command')}")