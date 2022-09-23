#spiekbriefje Mart

#Variablen = stukje data van het type
#STR = Stukje text
#INT = Heel getal zonder decimalen
#FLOAT = Getal met decimalen

Dom = 'mart' #Voorbeeld van String
int = 9 #Voorbeeld van een Integer
float = 10.69 #Voorbeeld van een Float

#BIF = Built In Function
#Built in functions zijn functions die altijd in elke code gebruikt kunnen worden en zitten ingebouwd in de programeer taal

print('Hallo wereld!') #Een voorbeeld van BIF print

Naam = input('Wat is uw naam? ') #voorbeeld van BIF input

#Formatting word gebruikt vooral als je variablen wilt gebruiken in een print

print(f'Hallo {Naam} !') #Voorbeeld van formatting
print(f'{float:.0f}') #voorbeeld van afronding op 0 decimalen via formatting

#if else en elif
#if = als iets dan
#elif = anders
#else = anders maar sluitend 

if Naam == 'Mart': #een if statement
    print('Mart is echt cool')
else: #een else statement
    print(f'{Naam} waarom ben jij hier?')

#loops worden gebruikt om 1 of meerdere acties te herhalen
#for loop = een loop waar je zeker weet dat hij zo vaak iets moet doen
#while loop = een loop waar je niet zeker weet hoe vaak hij herhaald moet worden

for i in range(2): #voorbeeld van een for loop
    print('HALLO!')

while int >= 9: #voorbeeld van een while loop
    int += 1
    print('Hallo')
    if int == 13:
        break

#Break continue
# break stopt een stukje code maar niet het hele programma
#continue zorgt er voor dat een stukje code weer door gaat

#Raise error = stopt een hele code als het word getriggerd

stop = input('wilt u stoppen? ')
if stop == 'ja':
    raise NameError('Ratio')