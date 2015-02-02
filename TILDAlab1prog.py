from TILDAlab1klass import Place

#def readFile():
with open('geodatasw.txt', 'r', encoding = "utf-8") as file:
    files = file.read();
    filelist = files.split("\n\n")
    masterlist = []
    for each in filelist:
        c = each.split("\n")
        masterlist.append(c)
    return filelist, masterlist
    
    print(masterlist[1])


användare matar in search = "haparanda"

def find(search, objectlist):
    for item in objectlist:
        try:
            if item.name == search: 
                item = search
        except:
             print("Wrong. Try again.")
    return item

def timing(question):
    startTime = time.time()






#if __name__ == "main":
    #skriv tester haer