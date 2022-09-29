weekdagentuple = ("maandag", "dinsdag", "woensdag", "donderdag", "vrijdag", "zaterdag", "zondag")
werkdagentuple = ("maandag", "dinsdag", "woensdag", "donderdag", "vrijdag")
werkdagentupler = ("maandag", "dinsdag", "woensdag", "donderdag", "vrijdag")
weekdagentupler = ("zondag", "zaterdag", "vrijdag", "donderdag", "woensdag", "dinsdag", "maandag")
weekenddagentuple = ("zaterdag", "zondag")
weekenddagentupler = ("zondag", "zaterdag")

for i in range(7):
    print(weekdagentuple[i])
print(" ")
for i in range(7):
    print(weekdagentupler[i])
print(" ")
for i in range(5):
    print(werkdagentuple[i])
print(" ")
for i in range(5):
    print(werkdagentupler[i])
print(" ")
for i in range(2):
    print(weekenddagentuple[i])
print(" ")
for i in range(2):
    print(weekenddagentupler[i])
print(" ")