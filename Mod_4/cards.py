import random

deck = ["Harten 1", "Harten 2", "Harten 3", "Harten 4", "Harten 5", "Harten 6", "Harten 7", "Harten 8", "Harten 9", "Harten 10","Harten Boer", "Harten Vrouw", "Harten Koning", "Harten Aas","Ruiten 1", "Ruiten 2", "Ruiten 3", "Ruiten 4", "Ruiten 5", "Ruiten 6", "Ruiten 7", "Ruiten 8", "Ruiten 9", "Ruiten 10","Ruiten Boer", "Ruiten Vrouw", "Ruiten Koning", "Ruiten Aas","Schoppen 1", "Schoppen 2", "Schoppen 3", "Schoppen 4", "Schoppen 5", "Schoppen 6", "Schoppen 7", "Schoppen 8", "Schoppen 9", "Schoppen 10","Schoppen Boer", "Schoppen Vrouw", "Schoppen Koning", "Schoppen Aas","Klaveren 1", "Klaveren 2", "Klaveren 3", "Klaveren 4", "Klaveren 5", "Klaveren 6", "Klaveren 7", "Klaveren 8", "Klaveren 9", "Klaveren 10","Klaveren Boer", "Klaveren Vrouw", "Klaveren Koning", "Klaveren Aas", "Joker", "Joker"]

for i in range(7):
    kaart = random.choice(deck)
    print(f"kaart {i + 1} = {kaart}")
    deck.remove(kaart)
    
random.shuffle(deck)
print(" ")
print(f"deck (49 kaarten): {deck}")