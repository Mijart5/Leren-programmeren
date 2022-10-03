import random

mm = int(input("Hoeveel m&ms moeten in de zak?: "))

bag = {
    "rood" : random.randint(1,mm),
    "blauw" : random.randint(1,mm),
    "groen" : random.randint(1,mm),
    "bruin" : random.randint(1,mm),
    "geel" : random.randint(1,mm)
}

print(bag)

