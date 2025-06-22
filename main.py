from pi_controller_sim import PiController
from microbit_maqueen_sim import VirtualMaqueen
'''
PHASE 1 - Goal: Establish reliable communication between Raspberry Pi and micro:bit/Maqueen 

Due to lack of hardware, I have implemented a software simulation where Pi controller can sends commands, 
and the microbot:Maqueen robot receives the command and respond to the data received     
This simulates the data flow and logic that will occur between devices.

Here the architecture outlines for this simulated system

main.py - Performs the simulation, simulating main program flow
pi_controller_sim.py - Simulates the Raspberry Pi controller logic, Sends command
microbit_maqueen_sim.py - Simulates the micro:bit and Maqueen robot, logic, Sends receives the command and respond to command

This approach demonstrate my understanding of the required communication and control logic, can be adapted for real hardware in the future

'''

#####
if __name__ == "__main__":
    robot = VirtualMaqueen()
    pi = PiController(robot)

    commands = ["FWD", "LEFT", "FWD", "RIGHT", "STOP"] #PI Send the codes and then micro:bit/maqueen receives and respond to it
    for cmd in commands:
        pi.send_command(cmd)

print("Phase 1 simulation complete.")