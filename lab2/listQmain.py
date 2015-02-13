#7 1 12 2 8 3 11 4 9 5 13 6 10
#from listQfile import ListQ
from sortFile import Sort
from cardDict import cardDict

def main():
	question = input("Du har 5 kort. I vilken ordning vill du laegga dessa?")
	numbers = question.split()
	
	for n in numbers:
		if not n.isdigit():
			try:
				numbers[numbers.index(n)] = cardDict[n]
			except KeyError:
				print('Du angav ett eller flera kort som inte finns i kortleken!')

	x = Sort(numbers)
	print(x)

main()

    