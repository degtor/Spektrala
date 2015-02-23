class Bintree:
    def __init__(self):
        self.root = None

    def put(self, newvalue):
        self.root = putFunc(self.root, newvalue)

    def exists(self, value):
        return existsFunc(self.root, value)

    def write(self):
        writeFunc(self.root)
        print("\n")
        
class Node:
    def __init__(self, value):
        self.value = None
        self.left = None
        self.right = None
        
    def __str__(self):
        return str(self.value)

#Hjaelpfunktioner        
def putFunc(root, newvalue):#Lagger till vaerde pa raett plats i funktionen
    if root is None:
        root = Node(newvalue)
    else:
        if newvalue > root.value:
            if root.left is None:
                root.left = Node(newvalue)
            else:
                putFunc(root.left, newvalue)
        else:
            if root.right is None:
                root.right = Node(newvalue)
            else:
                putFunc(root.right, newvalue)
    return root
                
def existsFunc(root, x): #Letar upp varde och returnerar false eller true
    if root is None:
        return False
    if root.value == x:
        return True
    else:
        if x > root.value:
            if root.left is None:
                return False
            else:
                existsFunc(root.left, x)
        else:
            if root.right is None:
                return False
            else:
                existsFunc(root.right, x)

"""def writeFunc(root, x): #skriver ut hela trädet
    listanffs = []
    listanffs.append(root.value)
    if x > root.value:
        if root.left is None:
            pass
        else:
            writeFunc(root.left, value)
    else:
        if root.right is None:
            pass
        else:
            existsFunc(root.right, value)
        return listanffs
"""
    