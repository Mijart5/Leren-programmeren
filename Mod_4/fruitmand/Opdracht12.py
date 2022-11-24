from fruitmand import fruitmand
fruit_naam = ""
namen = {"yellow": "geel", "green": "groen", "orange": "oranje", "red": "rood", "brown": "bruin"}
for i in fruitmand:
    i["color"] = namen[i["color"]]

for i in fruitmand:
    if len(i["name"]) > len(fruit_naam):
        fruit_naam = i["name"]
        index = fruitmand.index(i)
print(f"{fruit_naam} ({len(fruit_naam)}) heeft een {fruitmand[index].get('color')} kleur en weegt {fruitmand[index].get('weight')} gram")