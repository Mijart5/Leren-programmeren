from fruitmand import fruitmand

kleuren = ""
for i in range(6):
    if fruitmand[i].get("color") not in kleuren:
        kleuren += fruitmand[i].get("color") + " "
    if fruitmand[i].get("name") == "druif":
        del fruitmand[i]
print(f"{kleuren} {fruitmand}")