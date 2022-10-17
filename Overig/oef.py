i = 0
stoppen = False
while stoppen == False:
    vraag = input("")
    if vraag == "STOP":
        i += 1
        print(f"u bent gestopt, counter staat op: {i}")
        break
    else:
        i += 1
        print(i)

x = 0
antwoord = ""
while antwoord != "STOP":
   antwoord = input("")
   x += 1
print(x)

for y in range(0,11):
    print(y)

i = 0
list = []
while i < 11:
    list.append({i})
    i += 1
print(list)