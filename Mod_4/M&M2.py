from random import randint

kleuren = ["rood", "blauw", "groen", "geel", "bruin"]
zak = []
amount = int(input("Hoeveel M&ms moeten in de zak?: "))

for x in range(amount):
    zak.append(kleuren[randint(0,4)])

bagofmms = {
    'rood' : zak.count('rood'),
    'blauw' : zak.count('blauw'),
    'groen' : zak.count('groen'),
    'geel' : zak.count('geel'),
    'bruin' : zak.count('bruin'),
}
print(bagofmms)


#zoek op random.choice