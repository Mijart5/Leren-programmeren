from RobotArm import RobotArm

robotArm = RobotArm('exercise 5')

# Jouw python instructies zet je vanaf hier:





# Na jouw code wachten tot het sluiten van de window:
robotArm.moveRight()
robotArm.grab()
for a in range(0,6):
    for a in range(0,8):
        robotArm.moveRight()
    robotArm.drop()
    for a in range(0,8):
        robotArm.moveLeft()
    robotArm.grab()

