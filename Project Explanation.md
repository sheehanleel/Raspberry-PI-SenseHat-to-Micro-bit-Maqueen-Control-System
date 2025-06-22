Copy of the docstring from my main.py
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

Phase 3 - Goal: Wrap existing functionality in ROS2 framework ( hopefully :) )

In this Phase 3 it will be my understanding of ROS2 publishing/subscriber setting, simulating the conversion of joystick input to a ROS2-compatible message
and passing it to the communication node that controls the Maqueen robot. As seen form the print runtime.

Implementation details:
The InputNode simulates the ROS2 publisher, reading mock SenseHat joystick input and converting it to a ROS2-compatible message or geometry_msgs/Twist message.
The CommNode acts as the ROS2 subscriber, receiving the message, processing the contents, and sending/issuing the correct command to the robot
As you may see there may no be a real ROS2 tools used, but this setup mirrors the structure and data flow of a real ROS2 robotic teleoperation.

The Simulation #Phase 3
It recreates ROS2's message flow using Python Class and function calls
Can be extended to use a real ROS2 messages and communication infrastructure with small/minimal code changes
Demonstrate a good understanding of how ROS2 nodes communicates and work together to be able to control the robot or enable robot control.

----------------------------------------------------------------------------------------------------------------------------------------------