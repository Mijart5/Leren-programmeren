save = []
i = 0

door = True
while door == True:
    nummero = (input("welk getal toevoegen aan de save?: "))
    save.append({nummero[i]})
    stop = input('wil je stoppen? ')
    print(save)
    if stop == 'ja':
        door = False
        break
i =+ 1
totaal = {save[0] + save[1]}
print(totaal)