from Process_geodata import Process_geodata	# importerar Process_data klassen som hanterar geodata-filerna

if __name__ == '__main__':

	def __main__():	# main-funktion som skriver ut en enkel meny som forklarar vilka val anvandaren kan gora
		print('Valkommen till Geodata-sokningen!')
		goedata = Process_geodata('geodataSW.txt') # Skapar en lista med objekt daer varje objekt representerar en plats fran geodata-filen

		while True:
			main_input = input('\n1: Sok efter plats\n2: Sok efter den sydligaste platsen\n3: Avsluta programmet\n\nValj: ') #Ber anvaendaren vaelja i "menyn"
			if main_input == '1':
				search_input = input('\nSok plats efter namn: ') # Ber anvaendaren att ange en soekterm 
				goedata.search_place(search_input) # Kallar pa search_place-metoden i Process_data-klassen som letar igeom alla objekt 		goedata-listan
			elif main_input == '2':
				goedata.find_southmost() # Kallar pa find_southmost-metoden som hittar den sydligaste platsen i geodata-filen och skriver ut resultatet
			elif main_input == '3':
				break # 
			else:
				print('\nFelaktig input, forsok igen!\n') # 

	__main__()