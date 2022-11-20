list = [5, 12, 19, 27, 3]
total = 0
list.append(25)
print(len(list), list)
list.remove(12)
print(list)
list.remove(5)
print(list)
list.insert(0,36)
print(list)
for i in range(5):
    total += list[i]
print(total)
list.clear()
print(list)
for x in range(1,4):
    list.append(x)
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