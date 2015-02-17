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
	# Om trädet är tomt kan ordet omöjligt finnas och funktionen returnerar False
	
	elif root.value == searchvalue:
		return True
	# Om root har samma värde som det sökta värdet har vi hittat det vi sökte och funktionen returnerar True
	
	elif searchvalue < root.value and root.left:
		return existsFunc(root.left, searchvalue)
	# Om root har ett barn åt vänster och det vi söker är mindre än värdet på root kallar vi på funktionen igen med barnet som root 
	
	elif searchvalue > root.value and root.right:
		return existsFunc(root.right, searchvalue)
	# Samma sak om det vi söker är större än värdet på root
	
	else:
		return False

def writeFunc(root):
	# Skriver ut trädet i ordningen genom att först skriva ut den vänstra delen av trädet, root och slutligen den högra delen av trädet
	if root:
	# Så länge root inte är None går vi nedåt i trädet, annars hoppar vi upp en nivå
		writeFunc(root.left)
		print(root.value)
		writeFunc(root.right)