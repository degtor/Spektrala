from linkedQfile import LinkedQ

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
q.put(1)
print("***** TEST 2 *****")
print("Forvaentar fel svar\n")
if q.isEmpty():
    print("q.isEmpty() ger raett svar.\n")
else:
    print("q.isEmpty() ger FEL svar.\n")
    
#Kollar att get() funkar genom att isEmpty blir True igen..
q = LinkedQ()
q.put(1)
q.get()
print("***** TEST 3 *****")
print("Forvaentar raett svar\n")
if q.isEmpty():
    print("q.isEmpty() ger raett svar.\n")
else:
    print("q.isEmpty() ger FEL svar.\n")