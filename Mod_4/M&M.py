import random

geheel = int(input("Hoeveel m&ms moeten in de zak?: "))
deel = geheel // 4
bag = (f"rood {deel}", f"groen {deel}", f"blauw {deel}", f"bruin {deel}")
zak = []

for i in range(4):
    zak.append({bag[i]})
print(zak)