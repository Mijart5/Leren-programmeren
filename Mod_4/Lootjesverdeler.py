import random
door = True
eerste_list = []

while door == True:
    naam = input("vul een naam in: ")
    eerste_list.append(naam)
    if input("wil je de lootjes verdelen? ") == "ja":
        if len(eerste_list) > 3:
            break
        else: 
            print("niet genoeg namen ingevuld")
            continue
tweede_list = eerste_list.copy()
random.shuffle(tweede_list)
aantal_keer = 0
while aantal_keer != len(eerste_list):
    for i in range(len(eerste_list)):
        if eerste_list[i] == tweede_list[i]:
            random.shuffle(tweede_list)
        else:
            print(eerste_list[i], tweede_list[i])
            aantal_keer += 1