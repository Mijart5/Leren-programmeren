import random
door = True
eerste_list = []
verdeling = {}


while door == True:
    naam = input("vul een naam in: ")
    eerste_list.append(naam)
    if input("wil je de lootjes verdelen? ") == "ja":
        if len(eerste_list) % 2 != 0:
            break
        else: 
            print("niet genoeg namen ingevuld")
            continue

tweede_list = eerste_list.copy()
random.shuffle(tweede_list)
for i in range(len(eerste_list)):
    verdeling.update({eerste_list[i] : tweede_list[i]})
print(verdeling)