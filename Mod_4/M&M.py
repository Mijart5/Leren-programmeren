import random 

MMtuple = ("oranje", "blauw", "groen", "bruin")

aantal_mm = int(input("hoeveel M&Ms worden toegevoegd aan de zak?: "))

A_oranje = random.randint(0,aantal_mm)
print(f"aantal oranje mms in de zak = {A_oranje}")
na_oranje = aantal_mm - A_oranje

A_blauw = random.randint(0,na_oranje)
print(f"aantal blauwe mms in de zak = {A_blauw}")
na_blauw = na_oranje - A_blauw

A_groen = aantal_mm - A_oranje - A_blauw
print(f"aantal groene mms in de zak = {A_groen}")