uren = float(input('hoe laat is het in uren? '))
minuten = float(input('hoe laat is het in minuten? '))
leftoveruren = 23 - uren
leftoverminuten = 60 - minuten

print(f'{leftoveruren} uren over en {leftoverminuten} minuten over')