from Place import Place
from operator import attrgetter
import time

class Process_geodata(): #Klass som hanterar inlasningen av data fran fil daer datan aer strukturerad pa ett specifikt saett.
	def __init__(self, input_file): #Init-attributen kraver att en fil ska laesas in.
		self.places = self.create_objects(self.process_file(input_file)) #Vid initiering skapas variabeln places som koers genom create_objects och processdata-metoderna med inlaest fil som argument.

	def process_file(self, input_file): #Metod som tar in fil, oppnar, laeser av och skapar listor i en lista
		processed_data = []
		with open(input_file, 'r', encoding = 'utf-8') as f: #Oppnar filen
			raw_data = f.read() #Laeser och sparar filen som en long straeng
			chunk_list = raw_data.split('\n\n') #Delar upp strangen vid varje dubbelt radbryt och lagger till en lista
		for chunk in chunk_list:
			place = chunk.split('\n') #delar foer varje element ater igen upp i listor for varje radbryt
			processed_data.append(place) #Lagger till element till listan processed_data
		return processed_data #Returnerar listor i en lista med relevanta data for varje objekt.

	def create_objects(self, processed_data): #Tar in fardiguppdelad data fran process_file-metoden och skapar objekt av datan.
		places = []
		for p in processed_data:
			try:
				place_obj = Place(p[0],p[1],p[2],p[3],p[4])#Forsoker skapa objekt med data utifran klassen Place.
				places.append(place_obj) #Lagger till objekt till lista places
			except:
				pass #Om inlaesning misslyckas, hoppa over.(Relevant for sista tomma raden t.ex.)
		return places #Returnerar lista med objekt

	def search_place(self, search_input): #Metod som behandlar anvandarens sokning av plats.
		t0 = time.time() #Startar tidtagning. Naer variablen skapas har den ett varde av x antal sekunder sedan arsskiftet och raknar sedan uppat.
		search_result = [place_obj for place_obj in self.places if place_obj.name == search_input] #Soker upp sokningen i objects-list och jamfor om sokt strang matchar nagot objekts .name
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
		southmost_place = min(self.places, key = attrgetter('latitude')) #Hittar med hjalp av attrgetter minsta vardet pa attributen latitude.
		search_time = time.time() - t0 #Avslutar tidtagning
		print('\nSoekningen tog ' + str(search_time) + ' sekunder\n')
		print(southmost_place)