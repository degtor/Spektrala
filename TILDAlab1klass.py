class Place():
    def __init__(self, name, description, latitude, longitude, update):
        self.name =  name
        self.description = description
        self.latitude = latitude
        self.longitude = longitude
        self.update = update
    
    def __str__(self):
        return str(self.name)
        
"""class ListFilter():
    def __init__(self, inputlist):
        self.inputlist = self.sortChunks(inputlist)
    
    def sortChunks(inputlist):
        with open(inputlist, 'r') as file:
            theFile = file.read()
            theFile = theFile.split('\n\n')
            objects = []
            for x in theFile:
                c = x.split('\n')
                objects.append(c)
        return objects[0]"""


c = Place("Hej",1,2,3,4)
d = Place("Hej2",1,2,3,4)
e = Place("Hej3",1,2,3,4)
lista = [c,d,e]
print(lista[0])
print(d)
print(e)
a = 'geodataSW.txt'


