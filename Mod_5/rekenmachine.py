def addition(num1,num2):
    answer = num1 + num2
    return answer
def subtraction(num1,num2):
    answer = num1 - num2
    return answer
def multiplication(num1,num2):
    answer = num1 * num2
    return answer
def division(num1,num2):
    answer = num1 / num2
    return answer

num1 = float(input("voer nummer 1 in! "))
while True:
    choice = input("wat wilt u doen? A) getallen optellen, B) getallen aftrekken, C) getallen vermenigvuldigen, D) getallen delen, E) getal ophogen, F) getal verlagen, G) getal verdubbelen H) getal halveren, i) stoppen?")
    if choice == "a":
        num2 = float(input("Voer nummer 2 in! "))
        answer = addition(num1,num2)
        print(f"uw keuze was optellen {num1} + {num2} = {answer}")
        num1 = answer
    elif choice == "b":
        num2 = float(input("Voer nummer 2 in! "))
        answer = subtraction(num1,num2)
        print(f"uw keuze was aftrekken {num1} - {num2} = {answer}")
        num1 = answer
    elif choice == "c":
        num2 = float(input("Voer nummer 2 in! "))
        answer = multiplication(num1,num2)
        print(f"uw keuze was vermenigvuldigen {num1} x {num2} = {answer}")
        num1 = answer
    elif choice == "d":
        num2 = float(input("Voer nummer 2 in! "))
        answer = division(num1,num2)
        print(f"uw keuze was delen {num1} / {num2} = {answer}")
        num1 = answer
    elif choice == "e":
        num2 = 1
        answer = addition(num1,num2)
        print(f"uw keuze was ophogen {num1} + {num2} = {answer}")
        num1 = answer
    elif choice == "f":
        num2 = 1
        answer = subtraction(num1,num2)
        print(f"uw keuze was verlagen {num1} - {num2} = {answer}")
        num1 = answer
    elif choice == "g":
        num2 = 2
        answer = multiplication(num1,num2)
        print(f"uw keuze was verdubbelen {num1} x {num2} = {answer}")
        num1 = answer
    elif choice == "h":
        num2 = 2
        answer = division(num1,num2)
        print(f"uw keuze was halveren {num1} / {num2} = {answer}")
        num1 = answer
    elif choice == "i":
        print(f"uw laatste antwoord was {answer} tot de volgende keer")
        break