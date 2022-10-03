import random
aantal_mm = int(input("hoeveel M&Ms worden toegevoegd aan de zak?: "))

A_rood = random.randint(0,aantal_mm)
na_rood = aantal_mm - A_rood

A_blauw = random.randint(0,na_rood)
na_blauw = na_rood - A_blauw

A_groen = random.randint(0,na_blauw)
na_groen = na_blauw - A_groen

A_geel = random.randint(0,na_groen)
na_geel = na_groen - A_geel

A_bruin = na_geel

kleuren = ["rood", "blauw", "groen", "geel", "bruin"] #zit de kleur al in de dict? dan een update anders toevoegen

bag = {}
bag.update({kleuren[0]: A_rood})
bag.update({kleuren[1]: A_blauw})
bag.update({kleuren[2]: A_groen})
bag.update({kleuren[3]: A_geel})
bag.update({kleuren[4]: A_bruin})
print(bag)