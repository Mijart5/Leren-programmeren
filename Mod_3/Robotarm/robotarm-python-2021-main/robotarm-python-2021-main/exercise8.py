from RobotArm import RobotArm

robotArm = RobotArm('exercise 8')
robotArm.speed = 5
for i in range(7):
    robotArm.moveRight()
    robotArm.grab()
    robotArm.moveLeft()
    robotArm.drop()