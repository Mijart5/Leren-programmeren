def fibonacci(num1, num2, hoevaak):
    vol_fibo = []
    vol_fibo.append(num1)
    vol_fibo.append(num2)
    for items in range(1,hoevaak - 1):
        laatste_nu = vol_fibo[items -1] + vol_fibo[items] 
        vol_fibo.append(laatste_nu)
    gulden_snede = vol_fibo[-1] / vol_fibo[-2]
    return vol_fibo, gulden_snede
print(fibonacci(0,1,10))