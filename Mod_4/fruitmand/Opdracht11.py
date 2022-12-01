from fruitmand import fruitmand

rond = 0
niet_rond = 0
cont = False
while cont == False:
    kleur = input("Kies een kleur: ")
    for x in fruitmand:
        if kleur == x["color"]:
            cont = True
    if not cont:
        print(f"{kleur} zit niet in de fruitmand")
for i in fruitmand:
    if i["color"] in kleur:
        if i["round"]:
            rond += 1
        else:
            niet_rond += 1
if rond == niet_rond:
    print(f"Er zijn {rond} ronde en {niet_rond} niet ronde vruchten in {kleur}")
elif rond > niet_rond:
    print(f"Er zijn {rond - niet_rond} meer ronde vruchten dan niet ronde vruchten in de kleur {kleur}")
else:
    print(f"Er zijn {niet_rond - rond} meer niet ronde vruchten dan ronde vruchten in de kleur {kleur}")