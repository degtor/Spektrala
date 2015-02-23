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
        print('\nAnanas aer med i tradet!\n')
        
    print("traedet inneholler: \n")
    svenska.write()
    print("rooten aer: " + str(svenska.root))

main()