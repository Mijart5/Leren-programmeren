aantal_croissantjes = int(input('aantal croissantjes? '))
prijs_croissantjes = float(input('prijs croissantjes?'))
croissantjes = aantal_croissantjes * prijs_croissantjes

aantal_stokbroden = int(input('aantal stokbroden? '))
prijs_stokbroden = float(input('prijs stokbroden? '))
stokbroden = aantal_stokbroden * prijs_stokbroden

aantal_kortingsbonnen = int(input('aantal kortingsbonnen? '))
afprijzing_kortingsbonnen = float(input('afprijzing kortingsbonnen? '))
kortingsbonnen = aantal_kortingsbonnen * afprijzing_kortingsbonnen

print(f'De totaal prijs van de feestlunch = {croissantjes + stokbroden - kortingsbonnen}')
