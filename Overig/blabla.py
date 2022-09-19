pc_prijs = 55
console_prijs = 70
member_korting = 70 - 5

antwoord = input('ben je een console of PC gamer? ')
if antwoord == 'console':
    members = input('Heb je een memebership? ja of nee? ')
    if members == 'ja':
        print(member_korting)
    else: print(console_prijs)
elif antwoord == 'PC':
    print(pc_prijs)