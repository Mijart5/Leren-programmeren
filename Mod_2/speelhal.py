ticket = input(str('Hoeveel kost/en de ticket/s? '))
tijd_VIP_VR = input(str('Hoelang wilt u VIP VR gebruiken? '))
prijs_VIP_VR = input(str('Wat is de prijs van VIP VR? '))
personen = input(str('Met hoeveel persoon/en bent u? '))

totaal_prijs = (float(ticket)) * (int(personen)) + (float(tijd_VIP_VR)) / 5 * (float(prijs_VIP_VR))

print(f'totaal prijs = {totaal_prijs:.2f}')