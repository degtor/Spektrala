from bintreeFile import Bintree

def main():
	svenska = Bintree()

	with open('word3.txt', 'r', encoding = 'utf-8') as svenskfil:
		for rad in svenskfil:
			ordet = rad.strip()
			if not svenska.exists(ordet):
				svenska.put(ordet)
			# Om ordet inte finns i trädet lagras det i trädet
			if svenska.exists(ordet[::-1]) and ordet != ordet[::-1]:
				print(ordet + ' - ' + ordet [::-1])
			# Om ordet skrivet baklänges finns i trädet och ordet inte är ett palindrom skrivs det ut

main()