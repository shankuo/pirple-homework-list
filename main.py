"""
Title: Homework Assignment #4: Lists
Purpose: Write a function to ONLY append unique value to the myUniqueList list and return True. Non-uniquness value 
append to myLeftoves list and return False.

Note: Python's in operator not used 
"""

# Global variables
# Initialize the myUniqueList and myLeftovers or empty []
myUniqueList = []
myLeftovers = []
index = 0

# append ONLY unique value into a list
# 
def addToList(value):
    ''' value contains of any data type and return boolean True for value gets appended '''
    myUniqueList.append(value)
    return True

# append ONLY reject value (non-uniqueness)
#
def addToRejectList(value):
    ''' value contains any data type and return boolean False '''
    myLeftovers.append(value)
    return False

# Main
# Scenario #1 Unique values
# 1st element
# index = 0
value = 2
addToList(value)
index += 1
# 2nd element
# index = 1
value = 1
if myUniqueList[index - 1] != value:
    if addToList(value):
        index += 1
else:
    addToRejectList(value)

# 3rd element
# index = 2
value = "Hello"
if myUniqueList[index - 1] != value and myUniqueList[index - 2] != value:
    if addToList(value):
        index += 1
else:
    addToRejectList(value)

# 4th element
# index = 3  
value = 3
if myUniqueList[index -1 ] != value and myUniqueList[index -2] != value and myUniqueList[index - 3] != value:
    if addToList(value):
        index +=1
else:
    addToRejectList(value)
# print output
print("Scenario #1 Unique")
print(myUniqueList)
print(myLeftovers)

# Scenario #2 Duplicate values
# 5th element
# index = 3  
value = 2
if myUniqueList[index-1] != value and myUniqueList[index-2] != value and myUniqueList[index-3] != value and myUniqueList[index - 4] != value:
    if addToList(value):
        index +=1
else:
    addToRejectList(value)
# print output
print("Scenario #2 Duplicate")
print(myUniqueList)
print(myLeftovers)
