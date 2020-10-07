import random

isRunning = True
while ( isRunning ) :
	print("HERHAAL DIT!")

	num = random.randrange(5)
	if (num == 4) :
	    isRunning = False
else:

	print("Einde eerste while-loop")
