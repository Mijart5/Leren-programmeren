#Mart kooijman's pizzacalculator

klein = input(str('Hoeveel kleine pizzas wilt u? '))
medium = input(str('Hoeveel Medium pizzas wilt u? '))
groot = input(str('Hoeveel grote pizza wilt u? '))

prijs_klein = 6
prijs_medium = 11.49    #Prijzen volgens https://www.fastfoodprijslijst.nl/new-york-pizza-prijslijst/ pizza margherita
prijs_groot = 13.49 

totaal_prijs = (int(klein)) * prijs_klein + (int(medium)) * prijs_medium + (int(groot)) * prijs_groot




print(f'-------------------------------\n-{klein} kleine pizzas van {prijs_klein}€\n-{medium} medium pizzas van {prijs_medium}€\n-{groot} grote pizzas van {prijs_groot}€\n-totaal prijs = {totaal_prijs:.2f}€\n-------------------------------')