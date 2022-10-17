import random

MAX_RANDOM = 2

kleuren = ["Rood", "Blauw", "Groen", "Geel", "Bruin"]
results = {}
amount = int(input("Hoeveel M&ms moeten in de zak?: "))

while amount != 0:
    num = random.randint(0, min(amount, MAX_RANDOM))
    color = random.choice(kleuren)
    if not results.get(color): results.update({color: 0})
    results[color] += num
    amount -= num
print(results)