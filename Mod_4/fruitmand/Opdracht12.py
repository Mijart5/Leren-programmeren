from fruitmand import fruitmand
fruit_naam = ""
renamers = {"yellow": "geel", "green": "groen", "orange": "oranje", "red": "rood", "brown": "bruin"}
for fruit in fruitmand:
    fruit["color"] = renamers[fruit["color"]]

for i in fruitmand:
    if len(i.get("name")) > len(fruit_naam):
        fruit_naam = i.get("name")
        index = fruitmand.index(i)
print(f"{fruit_naam} ({len(fruit_naam)}) heeft een {fruitmand[index].get('color')} kleur en weegt {fruitmand[index].get('weight')} gram")