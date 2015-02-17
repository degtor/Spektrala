from bintreeFile import Bintree

def main():
	svenska = Bintree()

	with open('word3.txt', 'r', encoding = 'utf-8') as svenskfil:
		for rad in svenskfil:
			ordet = rad.strip()
			if svenska.exists(ordet):
				print(ordet, end = ' ')
			else:
				svenska.put(ordet)
	print('\n')

main()