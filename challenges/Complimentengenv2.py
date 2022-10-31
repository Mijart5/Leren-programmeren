from random import randint

naam = input("Wat is uw naam?: ")
vraag = input("Complimenten of beledigingen?: ")
aantal = int(input("Hoeveel?: "))
complimenten = ("Je bent geweldig!", "Goed gewerkt!", "Sick skills!", "Zo slim!")
beledigingen = ("Je bent kut", "je bent lelijk", "je eet poep voor ontbijt", "git gud", "je bent dik")
lcijfer = 0

if vraag == "complimenten":
    for i in range(aantal):
        cijfer = randint(0,3)
        while cijfer == lcijfer:
            cijfer = randint(0,3)
        print(f"{complimenten[cijfer]}, {naam}")
        lcijfer = cijfer
else:
    for i in range(aantal):
        cijfer = randint(0,4)
        while cijfer == lcijfer:
            cijfer = randint(0,4)
        print(f"{beledigingen[cijfer]}, {naam}")
        lcijfer = cijfer 