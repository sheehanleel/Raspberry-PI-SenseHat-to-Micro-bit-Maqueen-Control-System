from pi_controller_sim import PiController
from microbit_maqueen_sim import VirtualMaqueen
from sense_hat import SenseHat, mapping_event_command
import time
'''
----------------------------------------------------------------------------------------------------------------------------------------------

PHASE 1 - Goal: Establish reliable communication between Raspberry Pi and micro:bit/Maqueen 

Due to lack of hardware, I have implemented a software simulation where Pi controller can sends commands, 
and the microbot:Maqueen robot receives the command and respond to the data received     
This simulates the data flow and logic that will occur between devices.

Here the architecture outlines for this simulated system

main.py - Performs the simulation, simulating main program flow
pi_controller_sim.py - Simulates the Raspberry Pi controller logic, Sends command
microbit_maqueen_sim.py - Simulates the micro:bit and Maqueen robot, logic, Sends receives the command and respond to command

This approach demonstrate my understanding of the required communication and control logic, can be adapted for real hardware in the future

----------------------------------------------------------------------------------------------------------------------------------------------

PHASE 2 - Goal: Add SenseHAT joystick control without ROS complexity 
Added sense_hat.py mock simulation.

I extended the simulation to add SenseHAT joystick control without ROS complexity, further emulating real-world control system
In this phase it will simulate capturing joystick events, mapping them to movement commands, and sending the commands to the virtual Maqueen robot for
teleoperation.

Details of implementation:
1.Joystick event Simulation
Since I dont have any hardware available, I used a mock sense_hat.py to simulate the SenseHAT and its joystick event.
I have custom_events to simulate the joystick sequence directions as defined as a list of dictionaries, this allows me to simulate any series of user input
up, down, left, right, middle.

2.Direction Mapping
The joystick directions e.g left or right is mapped to its corresponding Maqueen Robot commands(check the runtime logs) using a dictionary in sense_hat.py "mapping_event_command"
This way approach it mirrors how joystick input would be processed on a real Raspberry Pi

3.Command Flow
Each simulated joystick event is processed in the main script "main.py"
The event is mapped to a robot command
The command is sent to Raspberry Pi controller simulation
Then the controller gives the command to the virtual Maqueen Robot, which responds accordingly in this case by printing the simulated joystick event.

4.Real-time Responsiveness
A quick short delay (time.sleep(0.5)) is added to get the same feeling of real user interaction.

----------------------------------------------------------------------------------------------------------------------------------------------
''' #Please Read the implementation and explanation Docstring

#####
if __name__ == "__main__":
    robot = VirtualMaqueen()
    pi = PiController(robot)

    # Phase 1 #


    commands = ["FWD", "LEFT", "FWD", "RIGHT", "STOP"] #PI Send the codes and then micro:bit/maqueen receives and respond to it
    for cmd in commands:
        pi.send_command(cmd)

    print("******************************************** Phase 1 Simulation Complete ********************************************")

    # Phase 1 #

    # Phase 2 #

    # Simulate teleoperation: map joystick directions to commands
    # Custom Joystick Movement
    custom_events = [
        {"direction": "right"},
        {"direction": "right"},
        {"direction": "left"},
        {"direction": "up"},
        {"direction": "middle"},
        {"direction": "down"},
        {"direction": "up"}
    ]
    sensehat = SenseHat(events=custom_events)

    for event in sensehat.stick.get_events():
        print("--------------------------")
        cmd = mapping_event_command.get(event["direction"], "STOP")
        print(f"[SenseHAT] Joystick: {event['direction']} -> Command: {cmd}")
        pi.send_command(cmd)
        time.sleep(0.5)
        print("--------------------------")

    print("******************************************** Phase 2 Simulation Complete ********************************************")




