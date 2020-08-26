# Lab 06, Problem 2
# nair0025, Namita Nair, lab section 007

def cntWordsOccur(sentences):
    newlist = []
    for i in sentences:
        sublist = []
        sublist.append(i)
        sublist.append(sentences.count(i))
        if sublist not in newlist:
            newlist.append(sublist)
    return newlist

def main():
    sentences = ['I', 'I', 'am', 'a', 'cat', 'dog', 'a', 'I']
    print(cntWordsOccur(sentences))
main()