from fruitmand import fruitmand

for i in fruitmand:
    if i.get("name") == "appel":
        print(fruitmand[fruitmand.index(i)].get("weight"))
        break