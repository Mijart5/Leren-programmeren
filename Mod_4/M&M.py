import random

geheel = int(input("Hoeveel m&ms moeten in de zak? (EVEN GETAL): "))

A_rood = random.randint(0,geheel)
na_rood = geheel - A_rood

A_blauw = random.randint(0,na_rood)
na_blauw = na_rood - A_blauw

A_groen = random.randint(0,na_blauw)
na_groen = na_blauw - A_groen

A_geel = random.randint(0,na_groen)
na_geel = na_groen - A_geel

A_bruin = na_geel

bag = (f"rood {A_rood}", f"groen {A_groen}", f"blauw {A_blauw}", f"bruin {A_bruin}")
zak = []

for i in range(4):
    zak.append({bag[i]})
print(zak)