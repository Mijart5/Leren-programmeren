antwoord = ""
vragen = True
while vragen == True:
    antwoord = input("Voer een antwoord in ")
    if antwoord in ("ja", "nee"):
        vragen = False
        print(antwoord)