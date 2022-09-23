getal1 = int(input('Geef getal 1 '))
getal2 = int(input('Geef getal 2 '))
actie = input('welke actie wenst u? (O) optellen (A) Aftrekken (KG) voor een volgorde van klein naar groot! (X) voor Keer (D) voor Delen: ')
zin = ''
if actie == 'O':
    antwoord = getal1 + getal2
elif actie == 'A':
    antwoord = getal1 - getal2
elif actie == 'KG':
    if  getal1 > getal2:
        zin = 'volgorde' + ' ' + str(getal2) + ' ' + str(getal1)
    else:
        zin = 'volgorde' + ' ' + str(getal1) + ' ' +str(getal2)
elif actie == 'X':
    antwoord = getal1 * getal2
elif actie == 'D':
    antwoord = getal1 / getal2
else:
    zin = 'Tik wat nuttigs in slimme jonge'


print(zin)
if actie == 'A' or 'O' or 'X' or 'D':
    print(antwoord)