bedrag = float(input("Voer een bedrag in: ")) * 100

euro_2 = bedrag // 200
print(f"munten van 2 euro {euro_2}")
restant = bedrag - 200 * euro_2

euro_1 = bedrag // 100
print(f"munten van 1 euro {euro_1}")
restant = bedrag - 100 * euro_1

cent_50 = bedrag // 50
print(f"munten van 50 cent {cent_50}")
restan = bedrag - 50 * cent_50

cent_20 = bedrag // 20
print(f"munten van 20 cent {cent_20}")
restant = bedrag - 20 * cent_20

cent_10 = bedrag // 10
print(f"munten van 10 cent {cent_10}")
restant = bedrag - 10 * cent_10

cent_5 = bedrag // 5
print(f"munten van 5 cent {cent_5}")
restant = bedrag - 5 * cent_5

cent_2 = bedrag // 2
print(f"munten van 2 cent {cent_2}")
restant = bedrag - 2 * cent_2

cent_1 = bedrag // 1
print(f"munten van 1 cent {cent_1}")
restant = bedrag - 1 * cent_1

print(f"de restant is {restant}")
