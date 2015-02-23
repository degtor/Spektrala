from bintreeFile import Bintree, Node
svenska = Bintree()              # Skapa ett trädobjekt
svenska.put("gurka")		    # Sortera in "gurka" i trädet	
if svenska.exists("gurka"):      # Kolla om "gurka" finns i trädet
   svenska.write()                  # Skriver alla ord i bokstavsordning
