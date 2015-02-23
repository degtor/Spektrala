class ListQ:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def put(self, item):
        self.items.append(item)

    def get(self):
        return self.items.pop(0) #Returnerar forsta vardet i koen.
        
