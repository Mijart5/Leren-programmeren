import random
spellen = 0
rondes = 0
while spellen >= 0:
    num = random.randint(0,1000)
    print(num)
    while rondes >= 0:
        gok = -1
        while gok == -1:
            try:
                gok = int(input("Voer een getal in: "))
            except ValueError:
                print("Dat is geen getal!")
        total = abs(num - gok)
        if gok == num:
            print('Wow! je hebt het nummer geraden')
            break
        if total <= 20:
            print('je bent heel warm')
        elif total <= 50:
            print('je bent warm')
        else:
            print('Koud raad nog eens!')
        rondes += 1
        print(f'{rondes} Rondes gespeeld')
        if rondes == 10:
            rondes -= 10
            break
    spellen += 1
    print(f'{spellen} spellen gespeeld')
    wiljestoppen = input('Wil je stoppen? (ja/nee): ')
    if wiljestoppen == 'ja':
        break
    if spellen == 20: 
        break