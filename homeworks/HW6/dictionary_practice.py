#Namita Nair, hw6

#==========================================
# Name: sameKeys
# Purpose: looks for keys found in both dictionaries and returns
#   a new dictionary with pairs where the key in the new dictionary
#   is the key found in both dictionaries
# Precondition: The dictionaries can have values of any type but the
#   function must keep data structures intact
# Input Parameter(s): (
#   diction1 - first dictionary of key:value pairs
#   diction2 - second dictionary of key:value pairs
# Return Value(s): 
#   -if both dictionaries are empty, return an empty dictionary
#   -new dictionary is return containing key:value pairs where the key
#   in the new dictionary is the key found in both dictionaries, with
#   the new value being a list of the values from both dictionaries
#============================================

def sameKeys(diction1, diction2):
    newdict = {}
    if diction1 == {} or diction2 == {}:
        return newdict
    for i in diction1.keys():
        for j in diction2.keys():
            if i == j:
                newlist = []
                newlist.append(diction1[i])
                newlist.append(diction2[i])
                newdict[i] = newlist
    return newdict

#==========================================
# Name: averageHours
# Purpose: takes in a dictionary of employees and their hours worked per
#   week, and returns a new dictionary with the average of their hours
# Precondition: Each keys value will either be a list of integers or an empty list
# Input Parameter(s): 
#   diction- a dictionary containing employees and their hours worked per week
# Return Value(s):
#   -if the dictionary is empty, return an empty dictionary
#   -new dictionary containing keys of the employees and values of their average
#   hours worked per week, the average being a truncated int
#============================================
    
def averageHours(diction):
    new_diction = {}
    if diction == {}:
        return new_diction
    for i in diction.keys():
        sum1 = 0
        ave = 0
        for j in diction[i]:
            sum1 += j
        if len(diction[i]) == 0:
            new_diction[i] = 0
        else:
            ave = int(sum1 / len(diction[i]))
            new_diction[i] = ave
    newlist = []
    for i in sorted (new_diction) :
        newlist.append(i)
        newlist.append(new_diction[i])
    return newlist

#==========================================
# Name: allKeys
# Purpose: takes in a dictionary with strings as keys and lists of integers
#    as values, and a list of integers. It returns a sorted list of non-
#   duplicated keys representing the keys from the dictionary where the 
#    integers on the element list were found to be one of the integers in the key's
#    value.
# Precondition: Each key will have as its value a list that is empty or a
#   list of integers. Element will never be empty.
# Input Parameter(s): 
#   diction-a dictionary with strings as keys and lists of integers as items
#   element- a list of integers
# Return Value(s):
#   -a new list of non-duplicated keys representing the keys from the dictionary 
#    where the any of the integers on the element list was found to be one of the 
#   integers in the key’s value
#============================================

def allKeys(diction, element):
    newlist = []
    for val in element:
        for i in diction.keys():
            if val in diction[i]:
                if i not in newlist:
                    newlist.append(i)
    return newlist

# yay :) 

        
            
            
    








































