import random
spellen = 0
rondes = 0
num = random.randint(0,1000)
print(num)
while spellen >= 0:
    while rondes >= 0:
        gok = int(input('Raad een nummer! '))
        if gok == num:
            print('Wow! je hebt het nummer geraden')
            break
        if num - gok <= 20:
            print('je bent heel warm')
        elif num - gok <= 50:
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
    if spellen == 20:
        break