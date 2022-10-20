import random
deck = []
spec = ("Koning", "Vrouw", "Boer", "Aas")
types = ("Harten", "Ruiten", "Schoppen", "Klaver")
for i in range(4):
    deck.append({types[0] : spec[i]})
    deck.append({types[1] : spec[i]})
    deck.append({types[2] : spec[i]})
    deck.append({types[3] : spec[i]})
    for y in range(2,11):
        deck.append({types[i]: {y}})
for i in range(7):
    kaart = random.choice(deck)
    print(f"kaart {i + 1} = {kaart}")
    deck.remove(kaart) 
random.shuffle(deck)
print(f"\ndeck 47 kaarten: \n{deck}")