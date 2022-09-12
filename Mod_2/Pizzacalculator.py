#Mart kooijman's pizzacalculator

try:
    klein = int(input('Hoeveel kleine pizzas wilt u? '))
except:
    print('Dat is geen nummer.')
try:
    medium = int(input('Hoeveel Medium pizzas wilt u? '))
except:
    print('Dat is geen nummer')
try:
    groot = int(input('Hoeveel grote pizza wilt u? '))
except:
    print('Dat is geen nummer')

try:
    prijs_klein = float(input('Wat is de prijs van de kleine pizzas? '))
except:
    print('Dat is geen nummer.')
try:
    prijs_medium = float(input('Wat is de prijs van de medium pizzas? '))
except:
    print('Dat is geen nummer.')
try:
    prijs_groot = float(input('wat is de prijs van de grote pizzas? '))
except:
    print('Dat is geen nummer.')

totaal_prijs = klein * prijs_klein + medium * prijs_medium + groot * prijs_groot




print(f'-------------------------------\n-{klein} kleine pizzas van {prijs_klein}€\n-{medium} medium pizzas van {prijs_medium}€\n-{groot} grote pizzas van {prijs_groot}€\n-totaal prijs = {totaal_prijs:.2f}€\n-------------------------------')