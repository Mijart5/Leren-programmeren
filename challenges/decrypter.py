encrypt = "PXDMn!?BdNhP!?eZcoEgBCau!?rxHTfSX!?ixhbV!?cCnlUhFv!?hJFDB!?tDgC!? Uox!?jZzTXPyKq!?uPxQ!?icToHOtRJ!?sscVwqvSfhh!?ttOe!? mAR!?vFzorM!?ebsDQfLcjgR!?rKo!?wnW!?eJGlOGG!?rCTP!?kpVZmoQxP e!?tMohfLBnYtm!?!Vkm"
next = False
vraagteken_gevonden = False
uitroep_gevonden = False
woord = ""
for c in encrypt:
    if next:
        woord += c
        next = False
    vraagteken_gevonden = c == "?"
    next = vraagteken_gevonden and uitroep_gevonden
    uitroep_gevonden = c == "!"
print(woord)