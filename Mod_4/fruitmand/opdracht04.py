from fruitmand import fruitmand
import random

lijst = []
aantal = int(input("Aantal?: "))
for i in range(aantal):
    lijst.append(random.choice(fruitmand)["name"])
print(lijst)