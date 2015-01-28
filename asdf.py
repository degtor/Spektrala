import time
# Klass som skapar objekt. 

class Geodata():
	def __init__(self, name, description, latitude, longitude, date):
		self.name = name 
		self.description = description
		self.latitude = latitude
		self.longitude = longitude
		self.date = date

# Metod som gör vårt objekt till en sträng. 

	def __str__(self): 
		string =('\n'+'Plats: '+self.name+'\n'+'Beskrivning: ' +self.description+'\n'+'Latitud: '+self.latitude+'\n'+'Longitud: '+self.longitude+'\n'+'Datum: '+self.date+'\n')
		return string

# Metod som hämtar objektets attribut namn som sedan används för sökning

	def getName(self):
		name = self.name
		return name

# Klass med attributet objectList, en lista bestående av alla Geodataobjekt.
# Input är en textfil innehållande information om objekten i listan. 
# Har även metoder som behandlar listan.

class ListProcessor():
	def __init__(self, inputfile):
		self.objectList = self.createObjectList(inputfile)

# Metod som öppnar textfil och skapar objekt genom att kalla på klassen Geodata. 
# Objekten lagras self.objectList.

	def createObjectList(self, inputfile):
		objectList = []
		textfile  =open(inputfile, "r")
		for i in range(5):									# Läser igenom de första 6 raderna, men gör inget med dem
			textfile.readline()		
		for line in textfile:
			dataBlock = []
			for i in range(5):								# Läser in raderna 6 och 6, lägger dem i dataBlock. Om dataBlock
				line = textfile.readline()					# har alla attribut skapas ett objekt som lagras i objectList. 
				line = line.rstrip()						# Detta loopas sedan genom hela textfilen. 
				dataBlock.append(line)
			if len(line) >= 5:
				name = dataBlock[0]
				description = dataBlock[1]
				latitude = dataBlock[2]
				longitude = dataBlock[3]
				date = dataBlock[4]
				objekt = Geodata(name, description, latitude, longitude, date)
				objectList.append(objekt)
		return(objectList)

	# Metod som jämför användarens inmatade namn med objektens namn i objectList. 
	# Tar även tid på denna process. 

	def search(self, inputstring):
		t0 = time.time()
		on = True
		while on: 
			for i in range(len(self.objectList)):			
				if self.objectList[i].getName() == inputstring:
					processTime = time.time()-t0
					return(self.objectList[i], processTime)
					on = False
			return('Platsen finns ej', None)
			on = False

	# Returnerar sydligaste punkten genom att sortera listan efter longitud.

	def findSouth(self):
		t0 = time.time()
		self.objectList = sorted(self.objectList, key=lambda objects : objects.longitude)
		processTime = time.time()-t0
		return(self.objectList[0], processTime)

# --------------------------- MAIN -------------------------

def main():
	print("Hej och välkommen. Här kan du söka efter olika platser i Sverige!\n")
	objectList = ListProcessor("geodataSW.txt")									# Skapar objekten

	on = True
	while on == True:
		choice = input("Gör ett av följande val: \n 1.Sök efter plats \n 2.Visa sydligaste punkt\n 3.Avsluta \n Välj: ")
		
		if choice == "1":
			locationChoice = str(input("\nVilken plats vill du söka efter? "))	
			location, processTime = objectList.search(locationChoice)
			if processTime: 
				print(location)
				print("Processen tog:", processTime, "sekunder \n")
			else: 
				print(location)
		elif choice == "2":
			south, processTime = objectList.findSouth()
			print(south)
		elif choice == "3":
			print("Hejdå")
			on = False
		else:
			print("Fel val, försök igen")

main()

