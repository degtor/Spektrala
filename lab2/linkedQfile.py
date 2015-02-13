class LinkedQ():

   def __init__(self): #Naer lankade listan skapas aer den tom och forsta och sista plats i listan aer alltso None.
      self.first = None
      self.last = None

   def __str__(self): #Straengmetod som skriver ut hela listan.
      s = ''
      p = self.first
      while p != None:
         s = s + str(p.value) + ' '
         p = p.next
      return s

   def put(self, x): #Metod som tar in varde x, skapar en nod av vardet och initialt ingen lankning(forens en ny nod skapas).
      node = Node(x)
      if self.first is None: #Satter sistaplatsen=forstaplatsen om forstaplatsen aer tom.
         self.first = self.last = node
      else:
         self.last.next = self.last = node #Annars skapas en lankning mellan nya noden och den forra redan existerande.

   def get(self): #plockar ut och returnerar forsta noden ur listan 
      x = self.first.value
      self.first = self.first.next #Passar vidare forsta platsen till naesta nod i listan.
      return x

   def isEmpty(self): #Kollar om listan aer tom.
      return self.first == None #Forsoker returnera att forstaplatsen aer tom, ger False om self.first != None, True annars.

   def magicSort(self): #Metod som skoter sjalva "raett-sorteringen av listan"
      s = ''
      while not self.isEmpty():
         self.put(self.get()) #Lagger forsta noden sist i listan
         p = self.get() #Returnerar nasta nod
         s = s + str(p) + ' ' #printar den.
      return s

class Node(): #Nod klassen, holler attribut for lankning och varde.

   def __init__(self, x):
      self.value = x
      self.next = None

   def __str__(self):
      return str(self.value)