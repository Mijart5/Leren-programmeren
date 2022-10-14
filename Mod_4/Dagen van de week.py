week = ("maandag", "dinsdag", "woensdag", "donderdag", "vrijdag", "zaterdag", "zondag")

print(week)
for i in range(5):
    print(week[i])
print("---------------")
print(week[5])
print(week[6])
print("---------------")

for i in range(6, 0, -1):
    print(week[i])
    i =- 1
print(week[0])
print("---------------")

for i in range(4, 0 ,-1):
    print(week[i])
print(week[0])
print("---------------")
print(week[6])
print(week[5])