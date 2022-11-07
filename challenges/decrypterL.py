crypt = "PXDMn!?BdNhP!?eZcoEgBCau!?rxHTfSX!?ixhbV!?cCnlUhFv!?hJFDB!?tDgC!? Uox!?jZzTXPyKq!?uPxQ!?icToHOtRJ!?sscVwqvSfhh!?ttOe!? mAR!?vFzorM!?ebsDQfLcjgR!?rKo!?wnW!?eJGlOGG!?rCTP!?kpVZmoQxP e!?tMohfLBnYtm!?!Vkm"
next = False
uitroepteken = False
vraagteken = False
result = []
for c in crypt:
    if next:
        result.append(c)
        next = False
    vraagteken = c == "?"
    next = vraagteken and uitroepteken
    uitroepteken = c == "!"
print(result)