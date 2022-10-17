import random

kleuren = ("Rood", "Groen", "Blauw", "Bruin")
aantal = int(input("Hoeveel M&Ms moeten toegevoegd worden aan de zak?: "))
zak = []

deel = random.randint(1,aantal)
ndeel = aantal - deel

deel2 = random.randint(1,ndeel)
ndeel2 = ndeel - deel2

deel3 = random.randint(1,ndeel2)
ndeel3 = ndeel2 - deel3

deel4 = random.randint(1,ndeel3)
ndeel4 = ndeel3 - deel4

A_bruin = ndeel4

print(f"{deel} {deel2} {deel3} {deel4} {deel + deel2 + deel3 + deel4}")

zak.append({kleuren[0] : deel})
zak.append({kleuren[1] : deel2})
zak.append({kleuren[2] : deel3})
zak.append({kleuren[3] : deel4})
print(zak)