#Mart kooijman's pizzacalculator
from asyncio.windows_events import NULL
from contextlib import nullcontext
from logging import NullHandler


klein = NULL
while not klein:
    try:
        klein = int(input('Hoeveel kleine pizzas wilt u? '))
        break
    except:
        print('Dat is geen nummer, probeer opnieuw.')
        continue

medium = NULL
while not medium:
    try:
        medium = int(input('Hoeveel Medium pizzas wilt u? '))
        break
    except:
        print('Dat is geen nummer, probeer opnieuw.')
        continue

groot = NULL
while not groot:
    try:
        groot = int(input('Hoeveel grote pizza wilt u? '))
        break
    except:
        print('Dat is geen nummer, probeer opnieuw.')
        continue

prijs_klein = NULL
while not prijs_klein:
    try:
        prijs_klein = float(input('Wat is de prijs van de kleine pizzas? '))
        break
    except:
        print('Dat is geen nummer, probeer opnieuw.')
        continue

prijs_medium = NULL
while not prijs_medium:
    try:
        prijs_medium = float(input('Wat is de prijs van de medium pizzas? '))
        break
    except:
        print('Dat is geen nummer, probeer opnieuw.')
        continue

prijs_groot = NULL
while not prijs_groot:
    try:
        prijs_groot = float(input('wat is de prijs van de grote pizzas? '))
        break
    except:
        print('Dat is geen nummer, probeer opnieuw.')
        continue

totaal_prijs = klein * prijs_klein + medium * prijs_medium + groot * prijs_groot




print(f'-------------------------------\n-{klein} kleine pizzas van {prijs_klein}€\n-{medium} medium pizzas van {prijs_medium}€\n-{groot} grote pizzas van {prijs_groot}€\n-totaal prijs = {totaal_prijs:.2f}€\n-------------------------------')