from RobotArm import RobotArm

robotArm = RobotArm('exercise 9')
robotArm.speed = 2

robotArm.grab()
for i in range(6):
    robotArm.moveRight()
robotArm.drop()
for i in range(5):
    robotArm.moveLeft()
robotArm.grab()
for i in range(4):
    robotArm.moveRight()
robotArm.drop()
for i in range(4):
    robotArm.moveLeft()
robotArm.grab()
for i in range(4):
    robotArm.moveRight()
robotArm.drop()
for i in range(3):
    robotArm.moveLeft()
robotArm.grab()
for i in range(2):
    robotArm.moveRight()
robotArm.drop()
for i in range(2):
    for i in range(2):
        robotArm.moveLeft()
    robotArm.grab()
    for i in range(2):
        robotArm.moveRight()
    robotArm.drop()