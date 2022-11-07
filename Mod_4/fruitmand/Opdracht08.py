from fruitmand import fruitmand

fruitmand.append({"Name" :"Watermeloen",
                     "weight" : 1300,
                     "color" : "green",
                     "round" : False
})
gewicht = 0
for i in range(8):
    gewicht += fruitmand[i].get("weight")
print(gewicht)