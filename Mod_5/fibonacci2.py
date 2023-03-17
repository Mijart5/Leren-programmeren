def fibo(num1,num2):
    lijst = []
    lijst.append(num1)
    lijst.append(num2)
    if len(lijst) == 10:
        return lijst
    else:
        return fibo(lijst[-1],lijst[-2])
print(fibo(0,1))