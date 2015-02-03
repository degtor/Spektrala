from Place import Place
from operator import attrgetter
import time

class Process_data(): #Klass som hanterar inlasningen av data fran fil daer datan aer strukturerad pa ett specifikt saett.
	def __init__(self, input_file): #Init-attributen kraver att en fil ska laesas in.
		self.objects_list = self.create_objects(self.process_data(input_file)) #Vid initiering skapas variabeln objects_list som koers genom create_objects och processdata-metoderna med inlaest fil som argument.

	def process_data(self, input_file): #Metod som tar in fil, oppnar, laeser av och skapar listor i en lista
		places = []
		with open(input_file, 'r', encoding = 'utf-8') as f: #Oppnar filen
			raw_data = f.read() #Laeser och sparar filen som en long straeng
			chunk_list = raw_data.split('\n\n') #Delar upp strangen vid varje dubbelt radbryt och lagger till en lista
		for chunk in chunk_list:
			place = chunk.split('\n') #delar foer varje element ater igen upp i listor for varje radbryt
			places.append(place) #Lagger till element till listan places
		return places #Returnerar listor i en lista med relevanta data for varje objekt.

	def create_objects(self, places): #Tar in fardiguppdelad data fran process_data-metoden och skapar objekt av datan.
		objects_list = []
		for place in places:
			try:
				place_obj = Place(place[0],place[1],place[2],place[3],place[4])#Forsoker skapa objekt med data utifran klassen Place.
				objects_list.append(place_obj) #Lagger till objekt till lista objects_list
			except:
				pass #Om inlaesning misslyckas, hoppa over.(Relevant for sista tomma raden t.ex.)
		return objects_list #Returnerar lista med objekt

	def search_place(self, search_input): #Metod som behandlar anvandarens sokning av plats.
		t0 = time.time() #Startar tidtagning. Naer variablen skapas har den ett varde av x antal sekunder sedan arsskiftet och raknar sedan uppat.
		search_result = [place_obj for place_obj in self.objects_list if place_obj.name == search_input] #Soker upp sokningen i objects-list och jamfor om sokt strang matchar nagot objekts .name
		search_time = time.time() - t0 #Avslutar tidning och tar skillnad mellan tiden fran arsskiftet och naer sokningen startades.

		if len(search_result) >= 1: #Om sokningen fick en eller flera traffar ska den skriva ut soktiden och vad sokningen hittade.
			print('\nSokningen tog ' + str(search_time) + ' sekunder och gav ' + str(len(search_result)) + ' traeffar:\n')
			for place_obj in search_result:
				print(place_obj)
				print('\n')
		else:
			print('\nSoekningen gav inga traeffar!\n')

	def find_southmost(self): #Metod som hittar den plats som enligt koordinaterna aer placerad laengst soder ut.
		t0 = time.time() #Start tidtagning
		southmost_place = min(self.objects_list, key = attrgetter('latitude')) #Hittar med hjalp av attrgetter minsta vardet pa attributen latitude.
		search_time = time.time() - t0 #Avslutar tidtagning
		print('\nSoekningen tog ' + str(search_time) + ' sekunder\n')
		print(southmost_place)