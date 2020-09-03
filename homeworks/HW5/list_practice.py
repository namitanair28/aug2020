# Namita Nair, hw5

#==========================================
# Name: cnt_occur
# Purpose: Takes in a list and returns the number of times an int
#   is on the list
# Precondition: The list contains different types of values and 
#   embedded lists
# Input Parameter(s): mylist-a list containing different values/lists
# Return Value(s): 
#   -returns 0 if there are no integers
#   -returns integer value of number of integers on the list
#============================================

def cnt_occur(mylist):
    if mylist == []:
        return 0
    elif isinstance(mylist[0], int):
        return 1 + cnt_occur(mylist[1:])
    elif isinstance(mylist[0], list):
        return cnt_occur(mylist[0]) + cnt_occur(mylist[1:])
    else:
        return cnt_occur(mylist[1:])

#==========================================
# Name: not_position
# Purpose: Takes in a list and an element and returns a list of
#   the index positions that do not contain the element
# Precondition: The list and the element are all integers
# Input Parameter(s): 
#   mylist-a list containing integers
#   num- an integer value
# Return Value(s): 
#   -returns a list containing the index positions
#============================================

def helper(mylist, num, count):
    if mylist == []:
        return []
    elif mylist[0] != num:
        return [count] + helper(mylist[1:], num, count+1)
    else:
        return helper(mylist[1:], num, count+1)
    
def not_position(mylist, num):
    return helper(mylist, num, 0)

#==========================================
# Name: seq_of_mult_3
# Purpose: models the recursive sequence that generates the sequence
#   {2, 6, 18, 54, 162...}
# Precondition: The input is a singular integer value
# Input Parameter(s): 
#   num- integer value
# Return Value(s): 
#   -returns an integer value
#============================================

def seq_of_mult_3(num):
    if num == 1:
        return 2
    else:
        return (3 * seq_of_mult_3(num-1))

#==========================================
# Name: create_range
# Purpose: creates a list containing all integers within a given range
# Precondition: the first number is less than or equal to the second
# Input Parameter(s): 
#   num1, num2 - the range of integers
# Return Value(s): 
#   -returns a list of all of the integers within the range
#============================================

def create_range(num1,num2):
    if num2 == num1:
        return [num1]
    else:
        return [num1] + create_range(num1+1, num2)





















