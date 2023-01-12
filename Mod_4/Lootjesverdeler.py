import random
eerste_list = []

while True:
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
ok = False
while not ok:
    random.shuffle(tweede_list)
    for i in range(len(eerste_list)):
        if eerste_list[i] == tweede_list[i]:
            ok = False
            break
        else:
            ok = True
print(eerste_list, tweede_list)