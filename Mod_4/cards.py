import random
deck = []
SPEC = ("Koning", "Vrouw", "Boer", "Aas")
TYPES = ("Harten", "Ruiten", "Schoppen", "Klaver")
for i in range(4):
    deck.append(TYPES[0] + " " + SPEC[i])
    deck.append(TYPES[1] + " " + SPEC[i])
    deck.append(TYPES[2] + " " + SPEC[i])
    deck.append(TYPES[3] + " " + SPEC[i])
    for y in range(2,11):
        deck.append(TYPES[i] + " " + str(y))
for i in range(7):
    kaart = random.choice(deck)
    print(f"kaart {i + 1} = {kaart}")
    deck.remove(kaart) 
random.shuffle(deck)
print(f"\ndeck 47 kaarten: \n{deck}")