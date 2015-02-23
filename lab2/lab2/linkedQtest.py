from linkedQfile import LinkedQ
from linkedQfile import Node

#Skapar en queue, init saeger att den ska skapas tom. isEmpty kollar att den aer tom.
q = LinkedQ()
print("\n***** TEST 1 *****")
print("Forvaentar ratt svar\n")
if q.isEmpty():
    print("q.isEmpty() ger raett svar.\n")
else:
    print("q.isEmpty() ger FEL svar.\n")

#Kollar att bade put() och isEmpty fungerar.
q = LinkedQ()
q.putFirst(1)
print("***** TEST 2 *****")
print("Forvaentar fel svar\n")
if q.isEmpty():
    print("q.isEmpty() ger raett svar.\n")
else:
    print("q.isEmpty() ger FEL svar.\n")
    
#Kollar att get() funkar genom att isEmpty blir True igen..
q = LinkedQ()
q.putFirst(1)
q.getFirst()
print("***** TEST 3 *****")
print("Forvaentar raett svar\n")
if q.isEmpty():
    print("q.isEmpty() ger raett svar.\n")
else:
    print("q.isEmpty() ger FEL svar.\n")
    
#Kollar att putLast och removeLast fungerar.
q = LinkedQ()
q.putLast(1)
q.putLast(2)
q.putLast(3)
q.removeLast()
print("***** TEST 4 *****")
print("Forvaentar raett svar\n")
if str(q) == '1 2 ':
    print("q.removeLast ger raett svar.\n")
else:
    print("q.removeLast ger FEL svar.\n")
    
#Kollar att putFirst och getfirst fungerar
q = LinkedQ()
q.putFirst(1)
q.putFirst(2)
q.putFirst(3)
x = q.getFirst()
print("***** TEST 5 *****")
print("Forvaentar raett svar\n")
if x == 3:
    print("q.getFirst ger raett svar\n")
else:
    print("q.getFirst ger FEL svar\n")
    
#Kollar att magic sort fungerar.
q = LinkedQ()
q.putFirst(1)
q.putFirst(3)
q.putFirst(2)
x = q.magicSort()
print("***** TEST 6 *****")
print("Forvaentar raett svar\n")
if str(x) == "3 2 1 ":
   print("q.magicSort() ger raett svar\n")
else:
   print("q.magicSort() ger FEL svar\n")