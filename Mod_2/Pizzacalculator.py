#Mart kooijman's pizzacalculator
from asyncio.windows_events import NULL
from contextlib import nullcontext
from logging import NullHandler


klein = None
while  klein == None:
    try:
        klein = int(input('Hoeveel kleine pizzas wilt u? '))
    except:
        print('Dat is geen nummer, probeer opnieuw.')

    print(klein)

medium = None
while  medium == None:
    try:
        medium = int(input('Hoeveel Medium pizzas wilt u? '))
    except:
        print('Dat is geen nummer, probeer opnieuw.')

groot = None
while groot == None:
    try:
        groot = int(input('Hoeveel grote pizza wilt u? '))
    except:
        print('Dat is geen nummer, probeer opnieuw.')

prijs_klein = None
while prijs_klein == None:
    try:
        prijs_klein = float(input('Wat is de prijs van de kleine pizzas? '))
    except:
        print('Dat is geen nummer, probeer opnieuw.')


prijs_medium = None
while prijs_medium == None:
    try:
        prijs_medium = float(input('Wat is de prijs van de medium pizzas? '))
    except:
        print('Dat is geen nummer, probeer opnieuw.')

prijs_groot = None
while prijs_groot == None:
    try:
        prijs_groot = float(input('wat is de prijs van de grote pizzas? '))
    except:
        print('Dat is geen nummer, probeer opnieuw.')

totaal_prijs = klein * prijs_klein + medium * prijs_medium + groot * prijs_groot




print(f'-------------------------------\n-{klein} kleine pizzas van {prijs_klein}€\n-{medium} medium pizzas van {prijs_medium}€\n-{groot} grote pizzas van {prijs_groot}€\n-totaal prijs = {totaal_prijs:.2f}€\n-------------------------------')