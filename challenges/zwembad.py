lengte = int(input("Wat is de lengte van uw zwembad?: "))
breedte = int(input("Wat is de breedte van uw zwembad?: "))
diepte = int(input("Wat is de diepte van uw zwembad?: "))
Grootte_zwembad = lengte * breedte * diepte

print(f'{Grootte_zwembad:.2f} M3')

uitgraaf_kosten = 25
uitgraaf_kosten = Grootte_zwembad * uitgraaf_kosten

afvoer_kosten = 32.50
afvoer_kosten = Grootte_zwembad * afvoer_kosten

totaal_graven = uitgraaf_kosten + afvoer_kosten

afstand = 60
if Grootte_zwembad < 20:
    voorrijkosten = 100
    if afstand < 50:
        voorrijkosten = voorrijkosten + afstand * 1.25
    elif afstand > 50:
        voorrijkosten = voorrijkosten +afstand * 1.15
else:
    voorrijkosten = 250
    if afstand < 50:
        voorrijkosten = voorrijkosten + afstand * 2.15
    elif afstand > 50:
        voorrijkosten = voorrijkosten + afstand * 2.05



print(f'''
Uitgraven: $ {uitgraaf_kosten:.2f}
Afvoeren: $ {afvoer_kosten:.2f}
Totaal: $ {totaal_graven:.2f}
Voorrijkosten: $ {voorrijkosten:.2f}
'''
)
