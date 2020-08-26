# Lab 06, Problem 4
# nair0025, Namita Nair, lab section 007

def usingWhileLoop(mylist):
    newlist = []
    numcount = 0
    strcount = 0
    elsecount = 0
    if mylist == []:
        return [0, 0, 0]
    while mylist:
        if isinstance(mylist[0], int) == True:
            numcount += 1
        elif isinstance(mylist[0], str) == True:
            strcount += 1
        else:
            elsecount += 1
        mylist.pop(0)
    newlist.append(numcount)
    newlist.append(strcount)
    newlist.append(elsecount)
    return newlist
    
def main():
    print(usingWhileLoop([1, 2, 3, 'a', 'b', 4]))
main()