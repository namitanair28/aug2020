# lab section 007, lab 5 stretch 1
# nair0025, Namita Nair

def listConstruction():
    wordlist = []
    word = input("Enter word: ")
    wordlist.append(word)
    while word != '':
        word = (input("Enter word: "))
        wordlist.append(word)
    wordlist.pop()
    newlist = []
    for i in wordlist:
        if i[0] in i[1:]:
            newlist.append(i)
    print(newlist)
    
listConstruction()
    
            
            
