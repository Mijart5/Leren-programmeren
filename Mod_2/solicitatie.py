dressuur = input('Hoeveel jaar ervaring heeft u met dieren-dressuur? ')
jongleren = input('hoeveel jaar ervaring heeft u met jongleren? ')
acrobatiek = input('hoeveel jaar ervaring heeft u met acrobatiek? ')
diploma = input('Welk MBO diploma heeft u? ')
rijbewijs = input('bent u in bezit van een geldig Vrachtwagen rijbewijs? ')
hoed = input('bent u in bezit van een hoge hoed? ')
man = input('bent u een man EN heeft u Snor breder dan 10 cm? ')
vrouw = input('bent u een vrouw met rood krulhaar langer dan 20cm? ')
lengte = input('Wat is uw lengte in centimeters? ')
gewicht = input('Wat is uw gewicht in kilogram? ')
certificaat = input('Heeft u certificaat “Overleven met gevaarlijk personeel”? ')

if dressuur == '4' or jongleren =='3' or acrobatiek == '3' and diploma == 'MBO-4 ondernemen' and rijbewijs == 'ja' and hoed == 'ja' and man == 'ja' or vrouw == 'ja' and lengte > 150 and gewicht > 90 and certificaat == 'ja':
    print('U voldoet aan de eisen')
else:
    print('U voldoet niet aan de eisen')