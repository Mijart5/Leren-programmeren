def voeren():
    naam_leeftijd = {}
    naam = str(input("voeg een naam toe ")) #voer naam in
    leeftijd = int(input("voeg een leeftijd toe ")) #voer leeftijd in
    naam_leeftijd["naam"] = naam #naam wordt toegevoegd aan dict
    naam_leeftijd["leeftijd"] = leeftijd #leeftijd wordt toegevoegd aan dict
    return naam_leeftijd #dict word gereturned
lijst = []
while True:
    lijst.append(voeren()) #dict wordt gecalled en toegevoegd aan de lijst
    if input("wilt u stoppen? ") == "ja": #hier wordt gevraag of je wilt stoppen
        break
for item in lijst:
    print(item["naam"] + " " + "is" + " " + str(item["leeftijd"]) + " " + "jaar oud") #print regel