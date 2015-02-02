class Stack:
    def __init__(self):
        self.top = None
        
    def push(self, x):
        ny = Node(x)
        ny.next = self.top
        self.top = ny
    
    def pop(self):
        x = self.top.value
        self.top = self.top.next
        return x
    
    def isempty(self):
        if self.top == None:
            return True
        else:
            return False

class Node:
    def __init__(self, x):
        self.value = x
        self.next = None
        

s = Stack()
print(s.isempty())
s.push(4)
print(s.isempty())
s.push(5)
print(s)
s.pop()
s.pop()
print(s.isempty())
