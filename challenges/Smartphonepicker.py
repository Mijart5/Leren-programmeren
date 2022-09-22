from telnetlib import GA


iphone13 = float(input('Hoe duur is de iPhone 13? '))
Galaxy22 = float(input('Hoe duur is de Galaxy 22? '))

if iphone13 > Galaxy22:
    print(f'De iphone 13 is het duurst, de telefoon kost: {iphone13:.2f} euro.')
    print(f'De Samsung Galaxy S22 is het goedkoopst, de telefoon kost: {Galaxy22:.2f} euro.')
    print(f'Het advies is dus om de Samsung Galaxy S22 te kopen. Deze is namelijk {iphone13 - Galaxy22:.2f} goedkoper.')
elif Galaxy22 > iphone13:
    print(f'De Samsung Galaxy S22 is het duurst, de telefoon kost: {Galaxy22:.2f} euro.')
    print(f'De iphone 13 is het goedkoopst, de telefoon kost: {iphone13:.2f} euro.')
    print(f'Het advies is dus om de iphone 13 te kopen. Deze is namelijk {Galaxy22 - iphone13:.2f} goedkoper.')
elif Galaxy22 > 900 and iphone13 > 900:
    print(f'De Iphone 13 kost {iphone13:.2f} euro.')
    print(f'De Samsung Galaxy S22 kost {Galaxy22:.2f} euro.')
    print('Ons advies is om geen telefoon te kopen, ze zijn te duur')
elif iphone13 == Galaxy22:
    print(f'De Iphone 13 kost: {iphone13:.2f}')
    print(f'De Samsung Galaxy S22 kost: {Galaxy22:.2f}')
    print('De prijzen zijn dus gelijk, ons advies is om de telefoon te kopen die u zelf wilt.')