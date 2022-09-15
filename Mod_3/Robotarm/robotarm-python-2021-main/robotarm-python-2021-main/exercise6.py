from RobotArm import RobotArm

robotArm = RobotArm('exercise 6')

robotArm.grab()
for a in range(0,6):
    robotArm.moveRight()
robotArm.drop()
for a in range(0,5):
    robotArm.moveLeft()
robotArm.grab()
for a in range(0,4):
    robotArm.moveRight()
robotArm.drop()
for a in range(0,3):
    robotArm.moveLeft()
robotArm.grab()
for a in range(0,5):
    robotArm.moveRight()
robotArm.drop()
for a in range(0,4):
    robotArm.moveLeft()
robotArm.grab()
for a in range(0,1):
    robotArm.moveRight()
robotArm.drop()