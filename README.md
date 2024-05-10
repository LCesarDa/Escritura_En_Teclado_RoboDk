
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


# Robot kinematics
## Denavit-Hartenberg parameters
Since we are using the UR5 robot in this case, we can obtain its forward kinematics manually or using Peter Corke's toolbox in MATLAB. With this, we obtain the following results

<p align="center">
 <img src="Multimedia/DH.jpeg" alt="Image Open" style="width:30%;"> 

 <p align="center">Denavid Hartenberg parameters obtained manually with the robot's zero position.



## Initial Setup

## Installation
First, we need to open RoboDK and generate the workspace. In this case, we decided to use the UR5, a welding table, and an STL CAD model of an HP keyboard. Actually, this program can be done solely with the robot and it's not necessarily required to use the UR5. It can be any robot from another brand or with different degrees of freedom, as long as it can reach the targets. For example, a SCARA robot might have trouble doing this, as well as a one-degree-of-freedom robot
 

To run this project you need the following components:

- RoboDK
- Virtual Robot UR5
- Virtual Table
- CAD of a Keyboard
- Python program
## Contact 

Authors:

Luis Fernando Cesar Denicia - luis.cesarda@udlap.mx - Github: LCesarDa

Jordán Joaquín Coronel Pérez - jordan.coronelpz@udlap.mx - Github: 

Jorge Zapata Hernández - jorge.zapatahz@udlap.mx - Github: JorgeZH1905

Project Link:


