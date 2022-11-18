from fruitmand import fruitmand
dict = {}
for i in (fruitmand):
    dict.update({i.get("weight"): i.get("name")})
print(sorted(dict.items(), reverse=True))