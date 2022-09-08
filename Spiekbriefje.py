# zo maak je commentaar

#||||||||||||||||||||||||||||||||||||
# dit zijn variablen
#||||||||||||||||||||||||||||||||||||

#aantal = 3   # dit is een integer
#omschrijving = "Lays naturel 300gr" #dit is een string
#prijs = 0.89 #dit is een float

#print(f'{aantal} {omschrijving} {prijs} totaal prijs = {aantal*prijs:.2f}')

#||||||||||||||||||||||||||||||||||||||
#Gebruik formatting
#\n is een newline
#f' :.2f' is een float met 2 decimalen
#||||||||||||||||||||||||||||||||||||||

#||||||||||||||||||||||||||||||||||||||
#Hoe kan dit korter worden?
#||||||||||||||||||||||||||||||||||||||

aantal = 3
omschrijving = "Lays naturel 300gr"
prijs = 0.89

Lays = f'{aantal} {omschrijving} {prijs} {aantal*prijs:.2f}'

print(Lays)