from bintreeFile import Bintree
from random import shuffle
import time
#Testar put
svenska = Bintree()
svenska.put('gurka')
if str(svenska.root) == "gurka":
    print("Root funkar")
else:
    print("Fel rot")

#Testar exists
if svenska.exists('gurka'):
	print('\nExists funkar!\n')
else: 
    print('\nExists funkar inte')

x = [[i] for i in range(1000000)]
shuffle(x)
position = 0
found = False
t0 = time.time()
while position < len(x) and not found:
    if x[position] == 5:
        found == True
    position = position + 1
searchtime = time.time() - t0
print(searchtime)

taltree = Bintree()
for b in x:
    taltree.put(b)
t0 = time.time()
taltree.exists([939])
searchtime = time.time() - t0
print(searchtime)