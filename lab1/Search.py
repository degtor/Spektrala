from Place import Place
from Process_data import Process_data
import time

class Search():
	def __init__(self, objects_list, search_input):
		self.objects_list = objects_list
		self.search_input = search_input

	def search_place(self):
		t0 = time.time()
		search_result = [place_obj for place_obj in self.objects_list if place_obj.name == self.search_input]
		search_time = time.time() - t0

		if len(search_result) >= 1:
			print('\nSökningen tog ' + str(search_time) + ' sekunder och gav ' + str(len(search_result)) + ' träffar:\n')
			for place_obj in search_result:
				place_obj.print_place()
				print('\n')
		else:
			print('\nSökningen gav inga träffar!\n')