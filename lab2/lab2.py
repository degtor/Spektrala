#7 1 12 2 8 3 11 4 9 5 13 6 10
from listQfile import ListQ
from sortFile import Sort

def main():
    question = input("Du har 5 kort. I vilken ordning vill du laegga dessa?")
    numbers = question.split()
    x = Sort(numbers)
    print(x.sortedList)

#if __name__== "main":
    #Skapar en queue, init saeger att den ska skapas tom. isEmpty kollar att den aer tom.
    #q = ListQ()
    #  if q.isEmpty():
     #     print("q.isEmpty() ger raett svar.")
     # else:
     #     print("q.isEmpty() ger FEL svar".)
main()

    