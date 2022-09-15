from RobotArm import RobotArm

robotArm = RobotArm('exercise 3')

# Jouw python instructies zet je vanaf hier:





# Na jouw code wachten tot het sluiten van de window:
for a in range(0,3):
    robotArm.grab()
    for a in range(0,9):
        robotArm.moveRight()
    robotArm.drop()
    for a in range(9,0,-1):
        robotArm.moveLeft()
    robotArm.grab()
