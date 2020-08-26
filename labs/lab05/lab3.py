# lab section 007, lab 05 stretch 2
# nair0025, Namita Nair

minlist = (input("Enter list: "))
num = input("Enter number: ")

def minimumIndex(minlist, num):
    newlist = minlist[num:]
    for i in newlist:
        if newlist[i] < newlist[i+1]:
            min = index(i)
    print(min)
    
minimumIndex(minlist, num)