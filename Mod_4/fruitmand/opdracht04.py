from fruitmand import fruitmand
import random

aantal = int(input("Aantal?: "))
for i in range(aantal):
    print(random.choice(fruitmand).get("name"))