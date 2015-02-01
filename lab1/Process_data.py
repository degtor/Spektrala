from Place import Place
from operator import attrgetter
import time

class Process_data():
	def __init__(self, input_file):
		self.objects_list = self.create_objects(self.process_data(input_file))

	def process_data(self, input_file):
		places = []
		with open(input_file, 'r', encoding = 'utf-8') as f:
			raw_data = f.read() 
			chunk_list = raw_data.split('\n\n') 
		for chunk in chunk_list:
			place = chunk.split('\n')
			places.append(place)
		return places

	def create_objects(self, places):
		objects_list = []
		for place in places:
			try:
				place_obj = Place(place[0],place[1],place[2],place[3],place[4])
				objects_list.append(place_obj)
			except:
				pass
		return objects_list

	def search_place(self, search_input):
		t0 = time.time()
		search_result = [place_obj for place_obj in self.objects_list if place_obj.name == search_input]
		search_time = time.time() - t0

		if len(search_result) >= 1:
			print('\nSökningen tog ' + str(search_time) + ' sekunder och gav ' + str(len(search_result)) + ' träffar:\n')
			for place_obj in search_result:
				print(place_obj)
				print('\n')
		else:
			print('\nSökningen gav inga träffar!\n')

	def find_southmost(self):
		t0 = time.time()
		southmost_place = min(self.objects_list, key = attrgetter('latitude'))
		search_time = time.time() - t0
		print('\nSökningen tog ' + str(search_time) + ' sekunder\n')
		print(southmost_place)