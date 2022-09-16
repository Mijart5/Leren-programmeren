quit = 1
while quit <= 5:
    antwoord = input('want to quit? ')
    if antwoord == 'yes':
        print(f'? {quit}') 
        quit += 1
    else:
        raise NameError('Too bad, you have to quit now')