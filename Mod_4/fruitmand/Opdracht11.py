from fruitmand import fruitmand

rond = 0
niet_rond = 0
cont = False
while cont == False:
    kleur = input("Kies een kleur: ")
    for x in range(7):
        if kleur in fruitmand[x].get("color"):
            cont = True
            break    
    print("kies een andere kleur")

for i in range(7):
    if fruitmand[i].get("color") in kleur:
        if fruitmand[i].get("round") == True:
            rond += 1
        else:
            niet_rond += 1
if rond == niet_rond:
    print(f"Er zijn {rond} ronde en {niet_rond} niet ronde vruchten in {kleur}")
elif rond > niet_rond:
    print(f"Er zijn {rond - niet_rond} meer ronde vruchten dan niet ronde vruchten in de kleur {kleur}")
else:
    print(f"Er zijn meer {niet_rond - rond} niet ronde vruchten dan ronde vruchten in de kleur {kleur}")