# Type help("robodk.robolink") or help("robodk.robomath") for more information
# Press F5 to run the script
# Documentation: https://robodk.com/doc/en/RoboDK-API.html
# Reference:     https://robodk.com/doc/en/PythonAPI/robodk.html
# Note: It is not required to keep a copy of this file, your Python script is saved with your RDK project

# You can also use the new version of the API:
from robodk import robolink    # RoboDK API
from robodk import robomath    # Robot toolbox
RDK = robolink.Robolink()

# Forward and backwards compatible use of the RoboDK API:
# Remove these 2 lines to follow python programming guidelines
from robodk import *      # RoboDK API
from robolink import *    # Robot toolbox
# Link to RoboDK
# RDK = Robolink()

RDK = Robolink() # establish a link with the simulator
robot = RDK.Item('UR5')      # retrieve the robot by name

# Program example:
item = RDK.Item('base')
if item.Valid():
    print('Item selected: ' + item.Name())
    print('Item posistion: ' + repr(item.Pose()))

print('Items in the station:')
itemlist = RDK.ItemList()
print(itemlist)

home = RDK.Item('Home')         # retrieve the Target item
robot.MoveJ(home)                 # move the robot to the target

ready = RDK.Item('Ready') 
robot.MoveJ(ready)               # linear move to the approach position

ins_call = mbox("Enter a program call to add after each movement", entry = "SynchRobot")

for caracter in ins_call:
    if caracter.isalpha():
        target = RDK.Item(caracter.upper())
        approach = target.Pose()*transl(0,0,-100)
        robot.MoveJ(approach)               # linear move to the approach position
        time.sleep(1)
        robot.MoveL(target)
        time.sleep(1)
        robot.MoveL(approach)

robot.MoveJ(ready)               # linear move to the approach position
robot.MoveJ(home)                 # move the robot to the target
