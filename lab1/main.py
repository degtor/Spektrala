from Process_data import Process_data	# importerar Process_data klassen som hanterar geodata-filerna

if __name__ == '__main__':

	def __main__():	# main-funktion som skriver ut en enkel meny som förklarar vilka val användaren kan göra
		print('Välkommen till Geodata-sökningen!')
		place_objects = Process_data('geodataSW.txt') # Skapar en lista med objekt där varje objekt representerar en plats från geodata-filen

		while True:
			user_input = input('\n1: Sök efter plats\n2: Sök efter den sydligaste platsen\n3: Avsluta programmet\n\nVälj: ') #Ber anvaendaren vaelja i "menyn"
			if user_input == '1':
				search_input = input('\nSök plats efter namn eller miljötyp: ') # Ber anvaendaren att ange en soekterm 
				place_objects.search_place(search_input) # Kallar på search_place-metoden i Process_data-klassen som letar igeom alla objekt i place_objects-listan
			elif user_input == '2':
				place_objects.find_southmost() # Kallar på find_southmost-metoden som hittar den sydligaste platsen i geodata-filen och skriver ut resultatet
			elif user_input == '3':
				break # 
			else:
				print('\nFelaktig input, försök igen!\n') # 

	__main__()