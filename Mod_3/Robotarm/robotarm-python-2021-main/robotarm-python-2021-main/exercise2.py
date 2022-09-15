from RobotArm import RobotArm

robotArm = RobotArm('exercise 2')

# Jouw python instructies zet je vanaf hier:





# Na jouw code wachten tot het sluiten van de window:
for a in range(0,4):
    robotArm.moveRight()
robotArm.grab()
for a in range(4,0,-1):
    robotArm.moveLeft()
robotArm.drop()
for a in range(0,7):
    robotArm.moveRight()
robotArm.grab()
for a in range(7,0,-1):
    robotArm.moveLeft()
robotArm.drop()