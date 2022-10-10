string1 = input("Wat is uw favoriete woord of zin?: ")
woord = ""
string2 = ""

for c in string1:
    if c == " ":
        string2 += woord + " " + woord + " "
        woord = ""
    else:
        woord += c
string2 += woord + " " + woord
print(string2)