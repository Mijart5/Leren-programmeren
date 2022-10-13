lengte = float(input("Wat is de lengte van uw zwembad?: "))
breedte = float(input("Wat is de breedte van uw zwembad?: "))
diepte = float(input("Wat is de diepte van uw zwembad?: "))
Grootte_zwembad = lengte * breedte * diepte

print(f'{Grootte_zwembad:.2f} M3')

uitgraaf_kosten = 25
uitgraaf_kosten = Grootte_zwembad * uitgraaf_kosten

afvoer_kosten = 32.50
afvoer_kosten = Grootte_zwembad * afvoer_kosten

totaal_graven = uitgraaf_kosten + afvoer_kosten

afstand = float(input("Wat is de afstand in KM?: "))
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

opp_zwembad = lengte * breedte
if Grootte_zwembad < 20:
    bet_teg = opp_zwembad * 250
    meerprijs_rood = input("Wilt u rode tegels?: ")
    if meerprijs_rood == "ja":
        bet_teg = bet_teg + opp_zwembad * 25
    meerprijs_kleurkeuze = input("Wilt u een kleur naar keuze voor uw tegels?: ")
    if meerprijs_kleurkeuze == "ja":
        bet_teg = bet_teg + 100
else:
     bet_teg = opp_zwembad * 200
     meerprijs_rood = input("Wilt u rode tegels?: ")
     if meerprijs_rood == "ja":
        bet_teg = bet_teg + opp_zwembad * 20
     meerprijs_kleurkeuze = input("Wilt u een kleur naar keuze voor uw tegels?: ")
     if meerprijs_kleurkeuze == "ja":
        bet_teg = bet_teg + 125

totaal = totaal_graven + voorrijkosten + bet_teg
print(f'''
Uitgraven: $ {uitgraaf_kosten:.2f}
Afvoeren: $ {afvoer_kosten:.2f}
Voorrijkosten: $ {voorrijkosten:.2f}
Beton + tegel {opp_zwembad:.2f}M2: $ {bet_teg:.2f}
Totaal: $ {totaal:.2f}
'''
)
