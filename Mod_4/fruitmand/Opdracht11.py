from fruitmand import fruitmand
rond = 0
niet_rond = 0
kleur = None
while kleur == None:
    kleur = input("Kies een kleur: ")
    if kleur not in ["yellow", "green", "orange", "red", "brown"]:
        kleur = None
        print("Kies een kleur uit de lijst")
    for i in range(7):
        if fruitmand[i].get("color") in kleur:
            if fruitmand[i].get("round") == True:
                rond += 1
            else:
                niet_rond += 1
if rond == niet_rond:
    print(f"Er zijn {rond} en {niet_rond} niet ronde vruchten in {kleur}")
elif rond > niet_rond:
    print(f"Er zijn {rond - niet_rond} meer ronde vruchten dan niet ronde vruchten in de kleur {kleur}")
else:
    print(f"Er zijn meer {niet_rond - rond} niet ronde vruchten dan ronde vruchten in de kleur {kleur}")