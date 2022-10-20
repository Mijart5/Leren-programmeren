import random

MAX_RANDOM = 2

kleuren = ["Rood", "Blauw", "Groen", "Geel", "Bruin"]
results = []
amount = int(input("Hoeveel M&ms moeten in de zak?: "))

for x in range(amount):
    num = random.randint(0, min(amount, MAX_RANDOM))
    color = random.choice(kleuren)
    results.append(color)
print(sorted(results))