doorgaan = True
while doorgaan == True:
    boodschappen = input("Wat wilt u halen?: ")
    aantal_boodschappen = input("hoeveel wilt u hiervan halen?: ")
    lijstje = {}
    lijstje.update({boodschappen: aantal_boodschappen})
    stoppen = input("wilt u stoppen?: ")
    if stoppen == "ja":
        print(f"{lijstje}")
        break