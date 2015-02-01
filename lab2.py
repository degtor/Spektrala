class ListQ:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        if self.items == []:
            return True
        else:
            return False

    def put(self, item):
        self.items.insert(-1,item)

    def get(self):
        return self.items.pop(0)
        
"""class Sort(ListQ):
    def __init__(self, unsortedList):
        self.unsortedList = unsortedList
    def magi(unsortedList):
       # [3 1 4 2 5] [12 1 8 2 10 3 7 4 9 5 11 6 13]
        unsortedList.put()
        unsortedList[0] = get()"""
        
    
def sort(x):
    

def main():
    question = input("Du har 5 kort. I vilken ordning vill du laegga dessa?")
    numbers = question.split()
    x = ListQ()
    for i in numbers:
        x.put(i)
    print(x.isEmpty())
    d  = Sort(x)
    print(d.magi())
  
  #  print("De kommer ut i ordningen: " + x[0] + x[1] + x[2] + x[3] +)
#if __name__== "main":
    #Skapar en queue, init säger att den ska skapas tom. isEmpty kollar att den är tom.
    #q = ListQ()
    #  if q.isEmpty():
     #     print("q.isEmpty() ger raett svar.")
     # else:
     #     print("q.isEmpty() ger FEL svar".)
main()
    