class LinkedQ():

   def __init__(self): #Naer lankade listan skapas aer den tom och forsta och sista plats i listan aer alltso None.
      self.first = None
      self.last = None
      self.length = 0

   def __str__(self): #Straengmetod som skriver ut hela listan.
      s = ''
      p = self.first
      while p != None:
         s = s + str(p.value) + ' '
         p = p.next
      return s

   def putLast(self,x): #Metod som tar in varde x, skapar en nod av vardet och initialt ingen lankning(forens en ny nod skapas).
      node = Node(x)
      if self.first is None: #Satter sistaplatsen=forstaplatsen om forstaplatsen aer tom.
         self.first = self.last = node
      else:
         self.last.next = self.last = node #Annars skapas en lankning mellan nya noden och den forra redan existerande.
      self.length += 1
   def isEmpty(self): #Kollar om listan aer tom.
      return self.first == None #Forsoker returnera att forstaplatsen aer tom, ger False om self.first != None, True annars.

   def removeLast(self):
      node = self.first
      for i in range(self.length - 2):
         node = node.next
      node.next= node.next.next
      self.last = node
      self.length -= 1

   def getFirst(self): #plockar ut och returnerar forsta noden ur listan 
      x = self.first.value
      self.first = self.first.next #Passar vidare forsta platsen till naesta nod i listan.
      self.length -= 1
      return x

   def putFirst(self,x):
      node = Node(x, self.first)
      self.first = node
      if self.last is None:
         self.last = node
      self.length += 1

   def isEmpty(self): #Kollar om listan aer tom.
      return self.first == None #Forsoker returnera att forstaplatsen aer tom, ger False om self.first != None, True annars.

   def magicSort(self): #Metod som skoter sjalva "raett-sorteringen av listan"
      s = ''
      while not self.isEmpty():
         self.putLast(self.getFirst()) #Lagger forsta noden sist i listan
         p = self.getFirst() #Returnerar nasta nod
         s = s + str(p) + ' ' #printar den.
      return s

class Node(): #Nod klassen, holler attribut for lankning och varde.

   def __init__(self, value, next = None):
      self.value = value
      self.next = next

   def __str__(self):
      return str(self.value)