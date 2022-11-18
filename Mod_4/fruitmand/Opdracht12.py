from fruitmand import fruitmand
fruit_naam = ""

fruitmand[0].update({"name": "ananas", "weight": 1590, "color": "geel", "round": False})
fruitmand[1].update({"name": "appel", "weight": 195, "color": "groen", "round": True})
fruitmand[2].update({"name" : "sinaasappel", "weight" : 130, "color" : "oranje", "round" : True})
fruitmand[3].update({"name" : "banaan", "weight" : 120, "color" : "geel", "round" : False})
fruitmand[4].update({"name" : "druif", "weight" : 5, "color" : "rood", "round" : True})
fruitmand[5].update({"name" : "kiwi", "weight" : 75, "color" : "bruin", "round" : False})
fruitmand[6].update({"name" : "citroen", "weight" : 100, "color" : "geel", "round" : True})

for i in fruitmand:
    if len(i.get("name")) > len(fruit_naam):
        fruit_naam = i.get("name")
        index = fruitmand.index(i)
print(f"{fruit_naam} ({len(fruit_naam)}) heeft een {fruitmand[index].get('color')} kleur en weegt {fruitmand[index].get('weight')} gram")