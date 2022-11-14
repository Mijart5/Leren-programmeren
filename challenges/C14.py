grootste = 0
kleinste = 1000
getal_d3 = 0
for i in range(10):
    getal = int(input("Voer een getal boven de nul en onder de duizend in: "))
    if getal > grootste:
        grootste = getal
    if getal < kleinste:
        kleinste = getal
    if getal % 3 == 0:
        getal_d3 += 1

print(f"het grootste getal is {grootste}\nhet kleinste getal is {kleinste} \nelk getal dat gedeeld door 3 kan worden zonder rest is {getal_d3} ")