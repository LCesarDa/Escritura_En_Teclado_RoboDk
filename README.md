
<a name="top"></a>
# Keyboard Input RoboDK
<p align="center">
  <img src="Multimedia/inicio.png" alt="Image Open" style="width:30%;"> 
</p>


<p align="center">Typing a word using a UR5 and a standard keyboard using a Python program in RoboDK.

## Project Overview
Programming in RoboDK provides precise control over the robot's behavior, enabling complex movements, conditional logic, and task automation. That's why Python programming is utilized in this project to enable our UR5 robot to type any word on the keyboard. The programming code will prompt the user to input the word to be typed by the UR5 robot when it reaches a specified position.
  
  
  
## Content List
- [Keyboard Input RoboDK](#keyboard-input-robodk)  
- [Project Overview](#project-overview)  
- [Requirements](#requirements)
- [Denavit-Hartenberg parameters](#denavit-hartenberg-parameters)
- [Initial Setup](#initial-setup)
- [Python programming](#python-programming)
- [Contact](#contact)

## Requirements
To run this project you need the following components:

- RoboDK
- Virtual Robot UR5
- Virtual Table
- CAD of a Keyboard
- Python program

## Denavit-Hartenberg parameters
Since we are using the UR5 robot in this case, we can obtain its forward kinematics manually or using Peter Corke's toolbox in MATLAB. With this, we obtain the following results

<p align="center">
 <img src="Multimedia/DH.jpeg" alt="Image Open" style="width:40%;"> 

 <p align="center">Denavid Hartenberg parameters obtained manually with the robot's zero position.


## Initial Setup

First, we need to open RoboDK and generate the workspace. In this case, we decided to use the UR5, a welding table, and an STL CAD model of an HP keyboard. Actually, this program can be done solely with the robot and it's not necessarily required to use the UR5. It can be any robot from another brand or with different degrees of freedom, as long as it can reach the targets.
<p align="center">
 <img src="Multimedia/workspace.jpeg" alt="Image Open" style="width:70%;"> 

 <p align="center">Robot workspace.
 
The next step, once we have everything set up as we want it, is to start adding the targets. It's worth noting that we used a closed gripper to simulate a finger pressing the keyboard, but it can definitely be done without it, although visually it may not look very good. In this case, we assigned three movements to set the positions of Home, Ready, and Approach that we can use for all movements. Below is the tree of operations along with the components used.

<p align="center">
 <img src="Multimedia/arbol.jpeg" alt="Image Open" style="width:50%;"> 

 <p align="center">RoboDK operation tree.

We can see that at the end of everything, we have a selected Python file. This will be responsible for allowing us to manipulate the robot to type the desired word.
It is also worth mentioning that for this case, we did not include the use of spaces or other special characters. However, if necessary, the corresponding targets can be generated and it should theoretically work without any extra changes to the code.

## Python programming

This Python script utilizes the RoboDK API to control a robotic arm, specifically targeting a UR5 robot. The script allows for movement to predefined targets and custom user-defined targets.

### Prerequisites

- Ensure you have RoboDK installed and configured.
- Python with RoboDK API must be installed.

### Usage

1. Open the Python script in a Python IDE or text editor.
2. Run the script (typically by pressing F5).
3. Follow the prompts to input a program call to add after each movement.
4. The robot will move accordingly based on the input provided.

### Additional Information

- **Documentation:** Detailed documentation for the RoboDK API is available [here](https://robodk.com/doc/en/RoboDK-API.html).
- **Reference:** For specific Python API references, refer to [this link](https://robodk.com/doc/en/PythonAPI/robodk.html).
- **Note:** You can find further details and guidelines within the script comments.

## Functionality

- The script establishes a connection with the RoboDK simulator.
- It retrieves the UR5 robot and predefined target items.
- Users need to input custom string names to execute after being in "Ready" position.
- The robot moves to approach positions for each letter typped in the input and back to ready and home positions as specified in the script.

## Contact 

Authors:

Luis Fernando Cesar Denicia - cesardenicialf@yahoo.com.mx - Github: LCesarDa

Jordán Joaquín Coronel Pérez - jordan.coronelpz@udlap.mx - Github: JordanCoronel

Jorge Zapata Hernández - jorge.zapatahz@udlap.mx - Github: JorgeZH1905

Project Link: https://github.com/LCesarDa/Escritura_En_Teclado_RoboDk.git


