# Lab 06, Problem 7
# nair0025, Namita Nair, lab section 007

def last_location(mylist, val):
    count = len(mylist)
    if val not in mylist:
        return None
    for i in range(len(mylist)-1, 0, -1):
        count -= 1
        if mylist[i] == val:
            return count

def main():
    print(last_location([1,2,2,4,4,6,4], 2))
main()