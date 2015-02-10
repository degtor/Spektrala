from sandbox import LinkedQ

def main():
	question = input("Du har 5 kort. I vilken ordning vill du laegga dessa?")
	numbers = question.split()
	linkedList = LinkedQ()
	for n in numbers:
		linkedList.put(n)
	print(linkedList.magicSort())
	#linkedList.put(linkedList.get())
	#linkedList.get()
	#linkedList.put(linkedList.get())
	#linkedList.get()
	#linkedList.put(linkedList.get())
	#linkedList.get()
	#linkedList.put(linkedList.get())
	#linkedList.get()
	#linkedList.put(linkedList.get())
	#linkedList.get()
	#if linkedList.isEmpty():
	#	print('Balle')	
main()