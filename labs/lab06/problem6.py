# Lab 06, Problem 6
# nair0025, Namita Nair, lab section 007

def IteratingLists(mylist):
    newlist = []
    for i in mylist:
        if isinstance(i, list) == True:
            for j in i:
                newlist.append(j)
    return newlist

def main():
    print(IteratingLists([[3]]))
main()