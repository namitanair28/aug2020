# Lab 06, Problem 7
# nair0025, Namita Nair, lab section 007

def location(mylist, val):
    count = -1
    if val not in mylist:
        return None
    for i in mylist:
        count += 1
        if i == val:
            return count

def main():
    print(location([1,2,2], 5))
main()