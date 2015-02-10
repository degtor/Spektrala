class LinkedQ():

   def __init__(self):
      self.first = None
      self.last = None

   def __str__(self):
      s = ''
      p = self.first
      while p != None:
         s = s + str(p.value) + ' '
         p = p.next
      return s

   def put(self,x):
      node = Node(x)
      if self.first is None:
         self.first = self.last = node
      else:
         self.last.next = self.last = node

   def get(self):
      x = self.first.value
      self.first = self.first.next
      return x

   def isEmpty(self):
      return self.first == None

   def magicSort(self):
      s = ''
      while not self.isEmpty():
         self.put(self.get())
         p = self.get()
         s = s + str(p) + ' '
      return s

class Node():

   def __init__(self, x):
      self.value = x
      self.next = None

   def __str__(self):
      return str(self.value)