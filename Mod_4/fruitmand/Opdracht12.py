from fruitmand import fruitmand
fruit_naam = ""

fruitmand[0].update({"name": "ananas","color": "geel"})
fruitmand[1].update({"name": "appel","color": "groen"})
fruitmand[2].update({"name" : "sinaasappel","color" : "oranje"})
fruitmand[3].update({"name" : "banaan","color" : "geel"})
fruitmand[4].update({"name" : "druif","color" : "rood"})
fruitmand[5].update({"name" : "kiwi","color" : "bruin"})
fruitmand[6].update({"name" : "citroen","color" : "geel"})

for i in fruitmand:
    if len(i.get("name")) > len(fruit_naam):
        fruit_naam = i.get("name")
        index = fruitmand.index(i)
print(f"{fruit_naam} ({len(fruit_naam)}) heeft een {fruitmand[index].get('color')} kleur en weegt {fruitmand[index].get('weight')} gram")