geheel = int(input("Hoeveel m&ms moeten in de zak? (EVEN GETAL): "))
deelr = geheel // 4
deelg = geheel // 4
deelb = geheel // 4
deelbr = geheel // 4
bag = (f"rood {deelr}", f"groen {deelg}", f"blauw {deelb}", f"bruin {deelb}")
zak = []

for i in range(4):
    zak.append({bag[i]})
print(zak)
