def get_input(text: str) -> float:
    while True:
      try:
        return float(input(text))
      except ValueError:
        print("Geef een nummer")

lengte = get_input("Wat is de lengte van uw zwembad?: ")
breedte = get_input("Wat is de breedte van uw zwembad?: ")
diepte = get_input("Wat is de diepte van uw zwembad?: ")
afstand = get_input("Wat is de afstand in KM?: ")
UITGRAAF_KOSTEN = 25
AFVOER_KOSTEN = 32.50
grootte_zwembad = lengte * breedte * diepte

print(f'Het zwembad is: {grootte_zwembad:.2f} M3')
print("----------------------------------------")
UITGRAAF_KOSTEN = grootte_zwembad * UITGRAAF_KOSTEN

AFVOER_KOSTEN = grootte_zwembad * AFVOER_KOSTEN

totaal_graven = UITGRAAF_KOSTEN + AFVOER_KOSTEN

if grootte_zwembad < 20:
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

opp_zwembad_LB = lengte * breedte
opp_zwembad_LH = lengte * diepte
opp_zwembad_HB = diepte * breedte

if grootte_zwembad < 20:
    bet_teg = opp_zwembad_LB + opp_zwembad_HB + opp_zwembad_LH * 250
    meerprijs_rood = input("Wilt u rode tegels?: ")
    if meerprijs_rood == "ja":
        bet_teg = bet_teg + opp_zwembad_LB + opp_zwembad_LH + opp_zwembad_HB * 25
    meerprijs_kleurkeuze = input("Wilt u een kleur naar keuze voor uw tegels?: ")
    if meerprijs_kleurkeuze == "ja":
        bet_teg = bet_teg + 100
else:
     bet_teg = opp_zwembad_LB + opp_zwembad_HB + opp_zwembad_LH * 200
     meerprijs_rood = input("Wilt u rode tegels?: ")
     if meerprijs_rood == "ja":
        bet_teg = bet_teg + opp_zwembad_LB + opp_zwembad_HB + opp_zwembad_LH * 20
     meerprijs_kleurkeuze = input("Wilt u een kleur naar keuze voor uw tegels?: ")
     if meerprijs_kleurkeuze == "ja":
        bet_teg = bet_teg + 125

totaal = totaal_graven + voorrijkosten + bet_teg
print(f'''----------------------------------------------------
- Uitgraven: $ {UITGRAAF_KOSTEN:.2f}
- Afvoeren: $ {AFVOER_KOSTEN:.2f}
- Voorrijkosten: $ {voorrijkosten:.2f}
- Beton + tegel {opp_zwembad_LB:.2f}M2: $ {bet_teg:.2f}
- Totaal: $ {totaal:.2f}
----------------------------------------------------
'''
)