# def vraag(vraag : str) -> str:
#     question = input(vraag)
#     return question
# antwoord = vraag("Voer iets in")
# print(antwoord.lower())

# def valiint(num : str) -> int:
#     while True:
#         try:
#             num = int(input(num))
#             break
#         except ValueError:
#             continue
#     return num
# validated = valiint("Voer een nummer in! ")
# print(validated, "is een integer")

# def loop(aantal : str) -> int:
#     while True:
#         try:
#             aantal = int(input(aantal))
#             break
#         except ValueError:
#             print("U heeft geen geldig nummer ingevuld!")
#             continue
#     for i in range(aantal):
#         aantal += i
#         print("iets")
#     return aantal
# aantal = loop("Voer in hoevaak je wilt herhalen")
# print(aantal)
# ans = None
# def question_validator(q1 : str , q2 : str) -> int:
#     q1 = int(input(q1))
#     q2 = int(input(q2))
#     if q1 == 6 and q2 == 9:
#         ans = True
#     else:
#         ans = False
#     return ans
# ans = question_validator("Voer een getal in: ", "Voer nog een getal in: ")
# print(ans)

def hallo_naam(zin : str) -> str:
    zin = "hallo" + " " + naam
    return zin

naam = input("vul je naam in ")
antwoord = hallo_naam("")

print(antwoord)