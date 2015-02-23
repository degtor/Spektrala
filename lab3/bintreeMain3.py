from bintreeFile import Bintree
from bintreeFile import Node

def main():
	svenska = Bintree()
	engelska = Bintree()

	with open('word3.txt', 'r', encoding = 'utf-8') as svenskfil:
		for rad in svenskfil:
			ordet = rad.strip()
			if not svenska.exists(ordet):
				svenska.put(ordet)

	with open('engelska.txt', 'r', encoding = 'utf-8') as engelskfil:
		for rad in engelskfil:
			ordrad = rad.split()
			for ordet in ordrad:
				if engelska.exists(ordet):
					pass
				else:
					engelska.put(ordet)
					if svenska.exists(ordet):
						print(ordet, end = ' ')
	print('\n')

main()