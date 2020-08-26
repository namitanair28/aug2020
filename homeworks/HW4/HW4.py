# Namita Nair, nair0025, Lab section 007
# Homework 4

# Problem 1
#==========================================
# Name: remove_the_fact
# Purpose: Given a list of strings, create a new list that has in
# position 0 the number of times “fact” was in the original list and in
# position 1, a list of all other strings in the original list that were
# not “fact”. There can be duplication of strings on the new list.
# Precondition: The list will only contain strings.
# Input Parameter(s)
# my_list: a list containing only strings or the empty list
# Return Value(s)
# -- if the input parameter is an empty list, return a list
# of [0, []]
# -- else return a list with the 0th index position containing the
# number of times “fact” was seen on the list and the 1st
# index position containing the list of the strings that are
# not “fact”. If there are no strings on the list, return
# an empty list in that position.
#============================================
def remove_the_fact(mylist):
    newlist = []
    newlist2 = []
    if mylist == []:
        newlist = [0, []]
        return newlist
    if 'fact' in mylist:
        count = mylist.count('fact')
        for string in mylist:
            if string != 'fact':
                newlist2.append(string)
        return [count, newlist2]
    if 'fact' not in mylist:
        return mylist
    
def main():
    mylist = ['cat', 'dog', 'apple']
    print(remove_the_fact(mylist))

# Problem 2
#==========================================
# Name: average_of_ints
# Purpose: Takes in a list of objects, and returns the average of all of the
#   ints in the list as well as a list of the ints themselves.
# Precondition: The list will contain a multitude of objects including ints
# Input Parameter(s)
# mylist: list inlcuding different types of objects including ints
# Return Value(s)
#   -list containing the average of the ints and a list of the ints themselves
#   -If list is empty, [0, []] is returned
#============================================
def average_of_ints(mylist):
    newlist = []
    intlist = []
    total = 0
    count = 0
    if mylist == []:
        emptylist = [0, []]
        return emptylist
    if int not in mylist:
        return [0, []]
    for object in mylist:
        if isinstance(object, int) == True:
            intlist.append(object)
            total += object
            count += 1
    newlist.append(int(total / count))
    newlist.append(intlist)
    return newlist

def main2():
    mylist = ['cat','dog']
    print(average_of_ints(mylist))

# Problem 3
#==========================================
# Name: max_of_lists
# Purpose: returns the maximum value in a list of lists
# Precondition: The list contains lists of numerical values.
# Input Parameter(s):
#   mylist: A list of lists containing numbers
# Return Value(s)
#   -A number, the maximum number within all of the lists in the list
#============================================
def max_of_lists(mylist):
    sublist = []
    maxlist = []
    if mylist == []:
        return 0
    for sublist in mylist:
        if sublist != []:    
            maxnum = sublist[0]
        for num in sublist:
            if maxnum < num:
                maxnum = num
                maxlist.append(maxnum)
    for num in maxlist:
        maxnum = maxlist[0]
        if maxnum < num:
            maxnum = num
    return maxnum             
    
def main3():
    mylist = [[], [2, 3], [0, -1, 3]]
    print(max_of_lists(mylist))

# Problem 4
#==========================================
# Name: greater_than
# Purpose: takes in a list and a numerical value, and checks to see
#   if all of the numerical elements of the list are greater than the value.
# Precondition: The list contains ints, floats, and strings. The single value
#   is a numeric value.
# Input Parameter(s):
#   mylist: list containing ints, floats, and strings
#   x: a numeric value
# Return Value(s)
#   -True if all values are greater than x, False if not
#============================================    
    
def greater_than(mylist, x):
    if mylist == []:
        return False
    for value in mylist:
        if isinstance(value, int) == True:
            if value >= x:
                return True
        if isinstance(value, float) == True:
            if value >= x:
                return True
        return False

def main4():
    mylist = [7, 'cat' , 5, 6]
    x = 4
    print(greater_than(mylist, x))
 
# Problem 5
#==========================================
# Name: selection_sort
# Purpose: Sorts a given list of integers from smallest to largest using
#   a selection-sort method but instead of swapping smallest values with
#   the first element, it swaps the largest value with the last element
# Precondition: The list contains only integers
# Input Parameter(s):
#   mylist: list of integers
# Return Value(s)
#   -mylist sorted from smallest to largest
#============================================    
    
def selection_sort(mylist):
    pos = 0
    maxval = 0
    for i in range (len(mylist) - 1, 0, -1):
        pos += 1
        for j in range(len(mylist)):
            if mylist[j] > mylist[i]:
                maxval = mylist[j]
                mylist[i], mylist[pos] = mylist[pos], mylist[i] 
    return mylist
    
def main5():
    mylist = [3, 5, 2, 8, 9, 1]
    print(selection_sort(mylist))
main5()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
