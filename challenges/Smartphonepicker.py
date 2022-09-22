from telnetlib import GA


iphone13 = float(input('Hoe duur is de iPhone 13? '))
Galaxy22 = float(input('Hoe duur is de Galaxy 22? '))
zenphone = float(input('Hoe duur is de Asus Zenphone? '))

if Galaxy22 > iphone13 and zenphone < Galaxy22:
    print(f'De Samsung Galaxy S22 is het duurst, de telefoon kost: {Galaxy22:.2f} euro.')
    print(f'De iphone 13 is het goedkoopst, de telefoon kost: {iphone13:.2f} euro.')
    print(f'De Zenphone zit er tussen in met: {zenphone:.2f} euro.')
elif iphone13 > Galaxy22 and zenphone < iphone13:
    print(f'De Iphone 13 is Het duurst, de telefoon kost {iphone13:.2f} euro.')
    print(f'De Samsung Galaxy S22 is het goedkoopst, de telefoon kost {Galaxy22:.2f} euro.')
    print(f'De zenphone zit er tussen in met: {zenphone:.2f} euro.')
if Galaxy22 > 899 and iphone13 > 899 and zenphone > 899:
    print(f'De Iphone 13 kost {iphone13:.2f} euro.')
    print(f'De Samsung Galaxy S22 kost {Galaxy22:.2f} euro.')
    print(f'De Zenphone kost: {zenphone:.2f} euro.')
    print('Ons advies is om geen telefoon te kopen, ze zijn te duur')
if iphone13 == Galaxy22 and Galaxy22 ==  zenphone and iphone13 == zenphone:
    print(f'De Iphone 13 kost: {iphone13:.2f}')
    print(f'De Samsung Galaxy S22 kost: {Galaxy22:.2f}')
    print(f'De Zenphone kost: {zenphone:.2f} euro.')
    print('De prijzen zijn dus gelijk, ons advies is om de telefoon te kopen die u zelf wilt.')