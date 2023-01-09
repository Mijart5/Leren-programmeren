Dict = {}

while True:
	naam = input("wat is uw naam?: ")

	if naam == "stop":
		break

	if naam in Dict:
		if input("Wil je bijwerken?: ") != "ja":
			continue

	leeftijd = int(input("Wat is uw leeftijd?: "))
	if leeftijd in Dict.values():
		print("er zit al iemand in die zo oud is")
		
	Dict[naam] = leeftijd

print(Dict)