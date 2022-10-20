import random

MAX_RANDOM = 2

kleuren = ["Rood", "Blauw", "Groen", "Geel", "Bruin"]
results = []
amount = int(input("Hoeveel M&ms moeten in de zak?: "))

while amount != 0:
    num = random.randint(0, min(amount, MAX_RANDOM))
    color = random.choice(kleuren)
    for I in range(num):
      results.append(color)
    amount -= num
print(sorted(results))