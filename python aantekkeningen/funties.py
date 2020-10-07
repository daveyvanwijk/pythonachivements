# Een basis vorm van een functie zonder speciale extra's. :)
def MijnFunctie():

	print("##############################################################")
	print("hallo, deze funtie wordt aangeroepen")
	print("Grappig hoor")
	print("##############################################################")

def FunctieMetParameters (waardeA, waardeB, waardeC) :

        print("waarde A is", waardeA)
        print("Waarde B is", waardeB)
        print("Waarde C is", waardeC)
        print("__________________________________")

#DIT MAG NIET, ALLE PARAMETERS DIE VOLGEN NA EEN PARAMETER MET EEN DEFAULT
# VALUE MOETEN OOK EEN DEFAULT VALUE HEBBEN!
#       print("MAG DAT?")
#       print(x)
#       print(y)
#       print(x)

def FunctieMetDefaultValues ( x, y = True, z = "leuk" ) :
        print("X is", x)
        print("Y is", y)
        print("Z is", z)


#voer de functie uit.
MijnFunctie()

getalA = 123
stukTekst = "Lachuh!"

#voer de functie met parameters uit met diverse argumenten:
FunctieMetParameters(True, 22, "stukTekst")
FunctieMetParameters(1, getalA, stukTekst)

#uitgevoerd waarbij de argumenten via het sleutelwoord (parameter naam) worden gegeven.
FunctieMetParameters(waardeC = 55, waardeA = False, waardeB = "0000")
print("==============================================================================")

# Functie met default values op verschillende wijzen aanroepen:
getalB = 55
FunctieMetDefaultValues("de eerste waarde 'x' moet")
FunctieMetDefaultValues("a", "b", "c")
FunctieMetDefaultValues(False, z = getalB)


