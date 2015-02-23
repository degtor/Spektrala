from bintreeFile import Bintree
startord = input("Vilket ord vill du borja med?")
slutord = input("Vilket ord vill du sluta med?")

def main():
	svenska = Bintree()
	gamla = Bintree()
	with open('word3.txt', 'r', encoding = 'utf-8') as svenskfil:
		for rad in svenskfil:
			ordet = rad.strip()
            if svenska.exists(ordet) == True:
                svenska.put(ordet)
            else:
                pass
    def makeChildren(x):
        alfabetet = "qwertyuiopåasdfghjklöäzxcvbnm"
        for tecken in alfabetet:
            for i in range(len(x)):
                child=x[:i]+tecken+x[i+1:]
                if svenska.exists(child) and not gamla.exists(child):
                    gamla.put(child)
                    print(child)

main()