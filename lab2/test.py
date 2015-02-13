from linkedQfile import LinkedQ

linkA = LinkedQ()
linkB = LinkedQ()

antal_kort = 7

for n in range(1,antal_kort + 1):
	linkA.putFirst(n)

linkB.putLast(linkA.getFirst())
linkB.putFirst(linkB.last)
linkB.removeLast()

while not linkA.isEmpty():
	linkB.putFirst(linkA.getFirst())
	linkB.putFirst(linkB.last)
	linkB.removeLast()

print(linkB)