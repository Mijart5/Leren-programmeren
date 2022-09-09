ticket = float(input('Hoeveel kost/en de ticket/s in euros? '))
tijd_VIP_VR = int(input('Hoelang wilt u VIP VR gebruiken in minuten? '))
prijs_VIP_VR = float(input('Wat is de prijs van VIP VR in euros? '))
personen = int(input('Met hoeveel persoon/en bent u? '))

totaal_prijs = ticket * personen + tijd_VIP_VR / 5 * prijs_VIP_VR

print(f'totaal prijs = {totaal_prijs:.2f}')