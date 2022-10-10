doorgaan = True
lijstje = {}
while doorgaan == True:
    item = input("Wat wilt u halen?: ")
    aantal_item = int(input("hoeveel wilt u hiervan halen?: "))
    try: 
        lijstje[item] = lijstje[item] + aantal_item
    except:
        lijstje.update({item: aantal_item})
    stoppen = input("wilt u stoppen?: ")
    if stoppen == "ja":
        print(f"{lijstje}")
        break