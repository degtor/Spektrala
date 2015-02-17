class Bintree():
    def __init__(self):
        self.root = None

    def put(self,newvalue):
        self.root = putFunc(self.root,newvalue)

    def exists(self,value):
        return existsFunc(self.root,value)

    def write(self):
        writeFunc(self.root)
        print("\n")

class Node():
	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None

	def __str__(self):
		return str(self.value)

def putFunc(root, newvalue):
    if root is None:
    	root = Node(newvalue)
    # Om trädet är tomt lagras ordet som root
    else:
    	if newvalue < root.value:
    	# Om ordet kommer före root i ordlistan tittar vi på barnet åt vänster
    		if root.left is None:
    			root.left = Node(newvalue)
    		# Om root saknar ett barn åt vänster lagras ordet där
    		else:
    			putFunc(root.left, newvalue)
    		# Om root har ett barn åt vänster kallar vi på putFunc med barnet som ny root
    	else:
    		if root.right is None:
    			root.right = Node(newvalue)
    		else:
    			putFunc(root.right, newvalue)
    		# Om ordet kommer efter root i ordlistan tittar vi på barnet åt höger och gör samma sak
    return root
    # Returnerar root för att skriva över objektets self.root-attribut

def existsFunc(root, searchvalue):
	if root is None:
		return False
	
	elif root.value == searchvalue:
		return True
	
	elif searchvalue < root.value and root.left:
		return existsFunc(root.left, searchvalue)
	
	elif searchvalue > root.value and root.right:
		return existsFunc(root.right, searchvalue)
	
	else:
		return False

def writeFunc(root):
	if root:
		writeFunc(root.left)
		print(root.value)
		writeFunc(root.right)