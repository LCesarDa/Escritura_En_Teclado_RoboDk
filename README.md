RoboDk program to write in a keyboard the inputed word
<a name="top"></a>
# Keyboard_Input_RoboDK
<p align="center">
  <img src="Images/inicio.png" alt="Image Open" style="width:30%;"> 
</p>


<p align="center">This is an implementation of a pick and place solution for the OpenManipulatorX.

## Project Overview
The Open MANIPULATOR-X robot based on ROS is one of the most commonly used robotic arms for training in the industry. In this project, a Pick and Place operation that will be performed using this robot arm. The goal is to create a program that instructs the robotic arm to pick up a series of objects and place them at a specific point in the workspace. Prior to this, a thorough analysis of the arm will be conducted to obtain its direct and inverse kinematics, and will be done using Matlab software in collaboration with the Robotics Toolbox plug-in developed by Peter Corke. For the Open MANIPULATOR-X will be used the teleoperation funtions to create a new project that execute the Pick and Place.
  
  
  
## Content List
- [Pick and Place](#pick-and-place)  
- [Project Overview](#project-overview)  
- [Requirements](#requirements)
- [Robot kinematics](#robot-kinematics)
  - [Denavit-Hartenberg parameters](#denavit-hartenberg-parameters)
  - [Obtaining and Validation of the Forward Kinematics and Inverse Kinematics using Matlab](#obtaining-and-validation-of-the-forward-kinematics-and-inverse-kinematics-using-matlab)
- [Initial Setup](#initial-setup)
  - [Installation](#installation)
  - [Open CR](#open-cr)
  - [Simulation](#simulation)
  - [Changes in the original project](#changes-in-the-original-project)
- [Add New Things](#add-new-things)
- [Important Links](#important-links)
- [Contact](#contact)
## Requirements

To run this project you need the following components:

- Ubuntu 20.04.
- ROS Noetic.
- Matlab.
- OpenManipulatorX.
- Open CR.
- Gazebo (Optional)
