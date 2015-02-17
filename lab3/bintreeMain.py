from bintreeFile import Bintree

def main():
	svenska = Bintree()
	svenska.put('gurka')
	svenska.put('ananas')
	svenska.put('ödla')
	svenska.put('gurra')
	svenska.put('tomat')
	svenska.put('luleå')
	svenska.put('choklad')

	
	if svenska.exists('ananas'):
		print('\nNICE!\n')

	svenska.write()
	print(svenska.root)

main()