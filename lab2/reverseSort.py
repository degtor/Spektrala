from linkedQfile import LinkedQ

def main():
	linkA = LinkedQ()
	linkB = LinkedQ()

	antal_kort = input('Hur många kort vill du sortera? ')

	for n in range(1,int(antal_kort) + 1):
		linkA.putFirst(n)

	while not linkA.isEmpty():
		linkB.putFirst(linkA.getFirst())
		linkB.putFirst(linkB.last)
		linkB.removeLast()

	return linkB

print(main())