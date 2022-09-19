from RobotArm import RobotArm

robotArm = RobotArm('exercise 7')
robotArm.speed = 4
for i in range(6):
    robotArm.moveRight()
    robotArm.grab()
    robotArm.moveLeft()
    robotArm.drop()
robotArm.moveRight()
for i in range(6):
    robotArm.moveRight()
    robotArm.moveRight()
    robotArm.grab()
    for i in range(2):
        robotArm.moveLeft()
    robotArm.drop()
for i in range(4):
    robotArm.moveRight()
robotArm.grab()
for i in range(3):
    robotArm.moveLeft()
robotArm.drop()
for i in range(5):
    for i in range(3):
        robotArm.moveRight()
    robotArm.grab()
    for i in range(3):
        robotArm.moveLeft()
    robotArm.drop()
for i in range(5):
    robotArm.moveRight()
robotArm.grab()
for i in range(4):
    robotArm.moveLeft()
robotArm.drop()
for i in range(5):
    for i in range(4):
        robotArm.moveRight()
    robotArm.grab()
    for i in range(4):
        robotArm.moveLeft()
    robotArm.drop()
for i in range(5):
    robotArm.moveRight()
robotArm.grab()
for i in range(4):
    robotArm.moveLeft()
robotArm.drop()
for i in range(6):
    for i in range(5):
        robotArm.moveRight()
    robotArm.grab()
    for i in range(5):
        robotArm.moveLeft()
    robotArm.drop()