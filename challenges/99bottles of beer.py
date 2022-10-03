i = 100
while i <= 100:
    print(f"{i} bottles of beer on the wall, {i} bottles of beer. Take one down and pass it around, {i-1} bottles of beer on the wall.")
    if i == 1:
        print(f"No more bottles of beer on the wall, no more bottles of beer. Go to the store and buy some more, 0 bottles of beer on the wall.")
        break
    i -= 1