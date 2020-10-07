print("hallo ik ben Davey, wat is jouw naam")
naam = input("typ hier je naam: ")
print("hallo " + naam)
wat = input("wat ga ik doen? \n A. naar school \n B. blijf thuis \n C. slapen")
	if wat == "A":
		school = input("wat ga ik op school doen? \n A. aan school \n B. spelletjes spelen")
			if school == "A" or "aan school":
				print("ik ga aan school en kom de dag door")
			else:
				spelletjes = input("wat ga ik spelen? \n A. solitair \n B. minecraft
					if spelen == "A":
						print("ik verveel me snel en gaat aan school")
					else:
						print("ik wordt gesnapt en gaat aan school")
	
	elif wat == "B":
		thuis = input("ga ik me ziek melden? \n A. ja \n B. nee
			if thuis == "A":
				print("ik wordt ziek gemeld door mijn moeder, maar ik moet nog steeds mee doen in de les via teams en mag nu 10 dagen niet meer naar buiten vanwege corona")
			else:
				print("mijn moeder ziet dat ik absent gemeld bent en belt school, ik mag nu 10 dagen niet meer naar buiten vanwege huis arrest")

	else:
		slapen = input("mijn moeder maakt me wakker en wilt dat ik naar school ga. wat ga ik doen? \n A. naar school \n B. naar buiten")
			if slapen == "A":
				print("ik ga naar school en kom heel laat en dat maakt het ongemakkelijk")
			else:
				print("mijn moeder ziet dat ik absent gemelt bent en belt school, ik mag nu 10 dagen niet meer naar buiten vanwege huis arrest")