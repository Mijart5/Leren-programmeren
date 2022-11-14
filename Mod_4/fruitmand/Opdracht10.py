from fruitmand import fruitmand
dict = {}
for i in range(7):
    dict.update({fruitmand[i].get("weight"): fruitmand[i].get("name")})
print(sorted(dict.items(), reverse=True))