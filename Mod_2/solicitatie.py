from distutils.log import error
from msilib.schema import Error


naam = input('wat is uw naam? ')
if naam == 'joe':
    raise NameError('joe mama')

leeftijd = int(input('hoe oud bent u? '))
if leeftijd == 69420:
    raise NameError('wow grapjas')

veter = input('kunt u uw veters strikken? ')
if veter == 'nee':
    raise NameError('L bozo')

dressuur = int(input('Hoeveel jaar ervaring heeft u met dieren-dressuur? '))
jongleren = int(input('hoeveel jaar ervaring heeft u met jongleren? '))
acrobatiek = int(input('hoeveel jaar ervaring heeft u met acrobatiek? '))
diploma = input('Welk MBO diploma heeft u? ')
rijbewijs = input('bent u in bezit van een geldig Vrachtwagen rijbewijs? ')
hoed = input('bent u in bezit van een hoge hoed? ')
man = input('bent u een man EN heeft u Snor breder dan 10 cm? ')
vrouw = input('bent u een vrouw met rood krulhaar langer dan 20cm? ')
lengte = int(input('Wat is uw lengte in centimeters? '))
gewicht = int(input('Wat is uw gewicht in kilogram? '))
certificaat = input('Heeft u certificaat “Overleven met gevaarlijk personeel”? ')

phase1 = False

if dressuur >= 4 or jongleren >= 3 or acrobatiek >= 3:
    phase1 = True

phase2 = False

if phase1 == True and diploma =='MBO-4 ondernemen' and rijbewijs == 'ja' and hoed == 'ja':
    phase2 = True

phase3 = False

if man == 'ja' or vrouw == 'ja':
    phase3 = True

if (lengte > 150 and gewicht > 90 and certificaat == 'ja'
    and phase1 == True and phase2 == True and phase3 == True):
    print('U voldoet aan de eisen')
else:
    print('u voldoet niet aan de eisen')