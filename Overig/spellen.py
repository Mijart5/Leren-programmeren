fysiek = input('is het een fysiek spel? (ja/nee): ')
if fysiek == 'ja':
    bordspell = input('is het een bordspel? (ja/nee): ')
    if bordspell == 'nee':
        kleur = input('is het spel oranje? (ja/nee): ')
        if kleur == 'ja':
            print('Het spel is sushi go!')
        else:
            print('het is een spel kaarten')
    else:
        treinen = input('heeft het spel treinen? (ja/nee): ')
        if treinen == 'ja':
            print('het spel is Ticket to Ride')
        else:
            print('het spel is Catan')
else:
    voetbal = input('is het een voetbal spel? (ja/nee): ')
    if voetbal == 'ja':
        print('het spel is FIFA')
    else:
        print('het spel is Age of empires IV')