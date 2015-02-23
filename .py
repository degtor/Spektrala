class Bintree:
    def __init__(self):
        self.root=None

    def put(self,newvalue):
        self.root=putFunc(self.root,newvalue)

    def exists(self,value):
        return existsFunc(self.root,value)

    def write(self):
        writeFunc(self.root)
        print("\n")