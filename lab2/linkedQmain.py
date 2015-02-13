from linkedQfile import LinkedQ

def main():
	question = input("Du har 5 kort. I vilken ordning vill du laegga dessa? ")
	numbers = question.split()
	linkedList = LinkedQ()
	for n in numbers:
		linkedList.putLast(n)
	print(linkedList.magicSort())
	
main()