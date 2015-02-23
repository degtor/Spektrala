from sortFile import Sort
from listQfile import ListQ

#Skapar en queue, init saeger att den ska skapas tom. isEmpty kollar att den aer tom.
q = ListQ()
print("\n***** TEST 1 *****")
print("Forvaentar ratt svar\n")
if q.isEmpty():
    print("q.isEmpty() ger raett svar.\n")
else:
    print("q.isEmpty() ger FEL svar.\n")

#Kollar att bade put() och isEmpty fungerar.
q = ListQ()
q.put(1)
print("***** TEST 2 *****")
print("Forvaentar fel svar\n")
if q.isEmpty():
    print("q.isEmpty() ger raett svar.\n")
else:
    print("q.isEmpty() ger FEL svar.\n")
    
#Kollar att get() funkar genom att isEmpty blir True igen..
q = ListQ()
q.put(1)
q.get()
print("***** TEST 3 *****")
print("Forvaentar raett svar\n")
if q.isEmpty():
    print("q.isEmpty() ger raett svar.\n")
else:
    print("q.isEmpty() ger FEL svar.\n")


numbers = [1,2,3]
print("***** TEST 4 *****")
print('Forvaentar raett svar\n')
x = Sort(numbers)
if str(x) == '2 1 3 ':
	print('q.magicSort() ger raett svar.\n')
else:
	print('q.magicSort() ger FEL svar.\n')
