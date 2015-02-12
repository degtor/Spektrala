#7 1 12 2 8 3 11 4 9 5 13 6 10
#from listQfile import ListQ
from sortFile import Sort

def main():
    question = input("Du har 5 kort. I vilken ordning vill du laegga dessa?")
    numbers = question.split()
    x = Sort(numbers)
    print(x.sortedList)

main()

    