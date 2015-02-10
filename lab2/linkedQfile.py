class LinkedQ(object):

    def __init__(self, first, last):
        self.head = None
        self.first = first
        self.last = last
        """Vilka attribut ska kön ha?"""

    def __str__(self):
	"""Returnerar köns element som en sträng."""
        s = ""
        p = self.first
        while p != None:
            s = s + str(p.value)
            p = p.next
        return s

    def put(self, item):
        x = Node(item)
        x.addNext(self.head)
        self.head = x
        """Stoppar in item sist i kön """

    def get(self):
        y = self.top.value
        self.top = self.top.next
        return y
        """Plockar ut och returnerar det som står först i kön """

    def isEmpty(self):
        return self.head == None
        """Returnerar True om kön är tom, False annars """
        
class Node:
    
    def __init__(self, dataValue):
        self.value = dataValue
        self.next = None
        
    def getValue(self):
        return self.value
        
    def nextNode(self):
        return self.next
    
    def addNext(self, newNext):
        self.next = newNext
    
    def addValue(self, newValue):
        self.value = newValue