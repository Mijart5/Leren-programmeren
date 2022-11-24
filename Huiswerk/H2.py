#counter = 0
#tafel = 1
#while counter != 13:
#    print(f"Tafel van {tafel}")
#    for multiplier in range(1,11):
#        print(tafel * multiplier)
#    counter += 1
#    tafel += 1

list = [5,12,19,27,3]
print(list)
list.append(25)
print(list)
print(len(list))
list.remove(12)
print(list)
list.pop(0)
print(list)
list.insert(0,36)
print(list)
totaal = 0
for i in range(5):
    totaal += list[i]
print(totaal)
list.clear()
print(list)
for i in range(1,4):
    list.append(i)
print(list)
for w in range(4,51):
    list.append(w)
print(list)
print(list[24])
list[0] = list[49]
list[49] = 1
print(list)
list2 = [1, "aap", 2, "apen", "watermeloen", 15, 27, "apen zijn fantastisch"]
for n in list2:
    if type(n) == int:
        print(n)