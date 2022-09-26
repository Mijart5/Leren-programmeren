import random
spellen = 0
rondes = 0
while spellen >= 0:
    spellen += 1
    print(f'{spellen} spellen gespeeld')
    while rondes >= 0:
        rondes += 1
        print(f'{rondes} Rondes gespeeld')
        if rondes == 10:
            rondes -= 10
            break
    wiljestoppen = input('Wil je stoppen? (ja/nee): ')
    if wiljestoppen == 'ja':
        break
    if spellen == 20: 
        break