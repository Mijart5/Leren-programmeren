import math
def water(liter: str) -> int:
    while True:
        try:
            tijd = float(input("voer een nummer in: "))
            break
        except:
            print("dat is geen geldig nummer!")
            continue
    liter = tijd * 0.5
    return math.floor(liter)
het = water("")
print(het)