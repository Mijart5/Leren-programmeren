from fruitmand import fruitmand

for i in range(7):
    if fruitmand[i].get("round"): #hoeft niet == true
        print(fruitmand[i].get("name"))