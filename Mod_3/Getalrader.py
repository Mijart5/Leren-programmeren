import random
spellen = 0
score = 0
while spellen >= 0:
    num = random.randint(0,1000)
    print(num)
    rondes = 0
    while rondes >= 0:
        gok = -1
        while gok == -1:
            try:
                gok = int(input('Voer een getal in: '))
            except ValueError:
                print('Dat is geen getal!')
        total = abs(num - gok)
        if gok == num:
            print('Wow! je hebt het nummer geraden')
            score += 1
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
            break
    spellen += 1
    print(f'{spellen} spellen gespeeld')
    door = input('Wil je doorgaan? (ja/nee) ')
    if door == 'ja':
        rondes = 0
        print(f'Je score tot nu toe is {score} getalen geraden over {spellen} spellen')
        continue
    elif door == 'nee':
        print(f'je score is {score} getalen geraden over {spellen} spel(len)')
        raise NameError('Je bent gestopt')
    if spellen == 20: 
        print(f'je score is {score} getalen geraden over {spellen} spellen')
        break