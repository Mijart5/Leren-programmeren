from fruitmand import fruitmand

fruitmand.append({"name" :"Watermeloen",
                     "weight" : 1300,
                     "color" : "green",
                     "round" : False #aangenomen dat watermeloenen ook ovaal kunnen zijn en dat zijn ze ook
})
gewicht = 0
for i in range(len(fruitmand)):
    gewicht += fruitmand[i].get("weight")
print(gewicht)