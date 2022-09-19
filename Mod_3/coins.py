toPay = int(float(input('Amount to pay: '))* 100) # om te betalem
paid = int(float(input('Paid amount: ')) * 100) # betaald
change = paid - toPay # wisselgeld

returned = {};

if change > 0: # als er wisselgeld is
  coinValue = 500 # 5 euro
  
  while change > 0 and coinValue > 0: # zolang er wisselgeld is en de waarde groter dan 0 is
    nrCoins = change // coinValue # aantal munten
    if coinValue > 100 and nrCoins > 0:
      print('return maximal ', nrCoins, ' coins of ', coinValue/100, ' euro!' ) # print het aantal munten en de waarde
      nrCoinsReturned = int(input('How many coins of ' + str(coinValue/100) +  ' euro did you return? ')) # vraag hoeveel munten er zijn teruggegeven
      change -= nrCoinsReturned * coinValue # bereken het wisselgeld
      returned[coinValue] = nrCoinsReturned
    elif nrCoins > 0: # als er munten zijn
      print('return maximal ', nrCoins, ' coins of ', coinValue, ' cents!' ) # print het aantal munten en de waarde
      nrCoinsReturned = int(input('How many coins of ' + str(coinValue) +  ' cents did you return? ')) # vraag hoeveel munten er zijn teruggegeven
      change -= nrCoinsReturned * coinValue # bereken het wisselgeld
      returned[coinValue] = nrCoinsReturned
# alle munten
    if coinValue == 500:
        coinValue = 200
    elif coinValue == 200:
        coinValue = 100
    elif coinValue == 50:
      coinValue = 20
    elif coinValue == 20:
      coinValue = 10
    elif coinValue == 10:
      coinValue = 5
    elif coinValue == 5:
      coinValue = 2
    elif coinValue == 2:
      coinValue = 1
    else:
      coinValue = 0
if change > 0: # als er nog wisselgeld is
  print('Change not returned: ', str(change) + ' cents')
else:
  print('done')
print(returned)