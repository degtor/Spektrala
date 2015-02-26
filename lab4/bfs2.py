from bintreeFile import Bintree
from linkedQfile import LinkedQ

q = LinkedQ()
svenska = Bintree()
gamla = Bintree()
startord = ParentNode(input("Vilket ord vill du börja med?, söt: "))
slutord = input("Vilket ord vill du sluta med?, sur: ")

class ParentNode:
    def __init__(self, word, parent = None):
        self.word = word
        self.parent = parent
        
    def writeChain(x):

        
with open ('word3.txt', 'r', encoding = 'utf-8') as svenskfil:
    for rad in svenskfil:
        ordet = rad.split()
        for orden in ordet:
            svenska.put(orden)    

def makeChildren(start, slut):
    ords = start.word
    alfabetet = 'qwertyuiopåasdfghjklöäzxcvbnm'
    for bokstav in alfabetet:
        for i in range(len(ords)):
            barn = ords[:i]+bokstav+ords[i+1:]
            if barn == slut:
                writeChain(barn)
                
            if svenska.exists(barn) and not gamla.exists(barn):
                gamla.put(barn)
                q.putLast(barn)

makeChildren(startord)

while not q.isEmpty():
    nod = q.getFirst()
    if nod == slutord:
        writeChain(nod)
        #print("Det finns en väg till", slutord)
    else:
        makeChildren(nod)
