class LinkedQ():

   def __init__(self):
      self.first = None
      self.last = None
      self.length = 0

   def __str__(self):
      s = ''
      p = self.first
      while p != None:
         s = s + str(p.value) + ' '
         p = p.next
      return s

   def putLast(self,x):
      node = Node(x)
      if self.first is None:
         self.first = self.last = node
      else:
         self.last.next = self.last = node
      self.length += 1

   def removeLast(self):
      node = self.first
      for i in range(self.length - 2):
         node = node.next
      node.next= node.next.next
      self.last = node
      self.length -= 1

   def getFirst(self):
      x = self.first.value
      self.first = self.first.next
      self.length -= 1
      return x

   def putFirst(self,x):
      node = Node(x, self.first)
      self.first = node
      if self.last is None:
         self.last = node
      self.length += 1

   def isEmpty(self):
      return self.first == None

   def magicSort(self):
      s = ''
      while not self.isEmpty():
         self.putLast(self.getFirst())
         p = self.getFirst()
         s = s + str(p) + ' '
      return s

class Node():

   def __init__(self, value, next = None):
      self.value = value
      self.next = next

   def __str__(self):
      return str(self.value)