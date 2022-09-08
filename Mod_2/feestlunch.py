aantal_croissantjes = input(str('aantal croissantjes? '))
prijs_croissantjes = input(str('prijs croissantjes?'))
croissantjes = (int(aantal_croissantjes)) * (float(prijs_croissantjes))

aantal_stokbroden = input(str('aantal stokbroden? '))
prijs_stokbroden = input(str('prijs stokbroden? '))
stokbroden = (int(aantal_stokbroden)) * (float(prijs_stokbroden))

aantal_kortingsbonnen = input(str('aantal kortingsbonnen? '))
afprijzing_kortingsbonnen = input(str('afprijzing kortingsbonnen? '))
kortingsbonnen = (int(aantal_kortingsbonnen)) * (float(afprijzing_kortingsbonnen))

print(f'De totaal prijs van de feestlunch = {croissantjes + stokbroden - kortingsbonnen}')
