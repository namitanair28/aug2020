# Lab 06, Problem 5
# nair0025, Namita Nair, lab section 007

def usingForLoop(mylist):
    newlist = []
    if mylist == []:
        return [0, 0, 0]
    numcount = 0
    strcount = 0
    elsecount = 0
    for i in mylist:
        if isinstance(i, int) == True:
            numcount += 1
        elif isinstance(i, str) == True:
            strcount += 1
        else:
            elsecount += 1
    newlist.append(numcount)
    newlist.append(strcount)
    newlist.append(elsecount)
    return newlist

def main():
    print(usingForLoop([1, 2, 3, 'a', 'b', 4]))
main()