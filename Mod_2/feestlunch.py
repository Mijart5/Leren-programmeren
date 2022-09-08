aantal_croissantjes = 17
prijs_croissantjes = 0.39
croissantjes = aantal_croissantjes * prijs_croissantjes

aantal_stokbroden = 2
prijs_stokbroden = 2.78
stokbroden = aantal_stokbroden * prijs_stokbroden

aantal_kortingsbonnen = 3
afprijzing_kortingsbonnen = 0.50
kortingsbonnen = 3 * 0.50

print(f'De totaal prijs van de feestlunch = {croissantjes + stokbroden - kortingsbonnen}')
