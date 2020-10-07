print("hallo ik ben Davey, wat is jouw naam")
naam = input("typ hier je naam: ")
print("hallo " + naam)
wat = input("wat ga ik doen? \n A. naar school \n B. blijf thuis \n C. ga slapen")
if wat == "A":
	ga = input("wat ga ik op school doen? \n A. spelletjes spelen \n B. opletten in de les/opdrachten maken: ")
	if ga == "A":
		spelen = input("wat ga ik spelen? \n A. solitair \n B. minecraft: ")
		if spelen == "A":
			print("ik verleelt je snel en gaat aan school")
		elif spelen == "B":
			print("ik wordt gesnapt en gaat aan school")
	else:
		print("ik ga aan school en kom de dag door")
elif wat == "B": 
	wat = input("ga ik me ziek melden? \n A. nee \n B. ja ")
		if wat == "A" or wat == "nee":
			print("ik wordt absent gemeld en m'n ouders zijn er niet blij mee")
		else:
			print("ik wordt ziek gemeld en moet 10 dagen thuis blijven vanwege corona en moet alnog meedoen met de les via teams")
elif wat == "C":
	slapen = input("mijn moeder wordt boos en wilt alnog dat ik naar school ga, ga ik naar school of naar buiten? \n A. naar school \n B. naar buiten")
 		if slapen = "A":
			print("ik komt veelste laat op school en het is heel ongemakkelijk, je gaat aan je opdrachten")
		else:
			print("ik wordt de heledag absent gemeld en besluit om het nooit meer te doen")
