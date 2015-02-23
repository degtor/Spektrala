from bintreeFile import Bintree
import random
import time

def main():
<<<<<<< HEAD
	svenska = Bintree()
	slumplista = random.sample(range(100000), 100000)
	for n in slumplista:
		svenska.put(n)
	while True:
		search = input('Sök efter ett nummer mellan 1-100000: ')
		t0 = time.time()
		if svenska.exists(int(search)):
			search_time = time.time() - t0	
			print('Binärsökningen tog ' + str(search_time*1000000) + ' mikrosekunder\n')

		t0 = time.time()
		for n in slumplista:
			if n == int(search):
				break
		print('Linjärsökningen tog ' + str((time.time() - t0)*1000000) + ' mikrosekunder\n')

		print(slumplista[0:10])
=======
    svenska = Bintree()
    svenska.put('gurka')
    svenska.put('ananas')
    svenska.put('ödla')
    svenska.put('gurra')
    svenska.put('tomat')
    svenska.put('luleå')
    svenska.put('choklad')
    
    if svenska.exists('ananas'):
        print('\nAnanas aer med i tradet!\n')
        
    print("traedet inneholler: \n")
    svenska.write()
    print("rooten aer: " + str(svenska.root))
>>>>>>> 21da2736d026dbb85f54511314f6ad63b9551424

main()