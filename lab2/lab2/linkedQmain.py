from linkedQfile import LinkedQ
from cardDict import cardDict

def main():
	question = input("Du har 5 kort. I vilken ordning vill du laegga dessa? ")
	numbers = question.split()
	linkedList = LinkedQ()
	
	for n in numbers:
		if not n.isdigit():
			try:
				numbers[numbers.index(n)] = cardDict[n]
			except KeyError:
				print('Du angav ett eller flera kort som inte finns i kortleken!')  

	for n in numbers:
		linkedList.putLast(n)
	print(linkedList.magicSort())
	
main()