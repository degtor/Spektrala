from listQfile import ListQ

class Sort(ListQ):
    def __init__(self, unsortedList):
        self.items = unsortedList
        self.sortedList = []
        self.magicSort()
        
    def magicSort(self):
        while not self.isEmpty():
            self.put(self.get())
            self.sortedList.append(self.get())        