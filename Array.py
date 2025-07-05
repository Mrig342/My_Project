#An array is a special variable, which can hold more than one value at a time. Array is a collection of items stored at contiguous memory locations. Array can only store one data type say 'int' or 'str'

# Create an int array and char array
from array import *

vals=array('i', [3,7,10,14,19,22,35])
vowels=array('u',['a','e','i','o','u'])

print(vals)
print(vowels)

# Show size and address of array
print(vals.buffer_info())
print(vowels.buffer_info())

# Show the type of array
print(vals.typecode)
print(vowels.typecode)

# Print any index value from the arrays
print(vals[4])
print(vowels[1])

# Print all values of an array
for e in vals:
    print(e)
for g in vowels:
    print(g)

# Copy vowels array to a new array
newArr=array(vowels.typecode, (a for a in vowels))
print(newArr)
# here "vowels.typecode" is used as we don't know the type of the array we are copying from

# Copy vals array to a new array with square of each number
NewArray=array(vals.typecode,(a*a for a in vals))
print(NewArray)

# Sort an array & add new value to the array
mig = array('i',[67,24,56,34,16,5])
print(mig)
print(sorted(mig))
mig.append(7)
print(mig)

# User defined array
mrig=array('i',[])
n=int(input('Enter the lenght of array'))

for x in range(n):
    x=int(input('Enter next value'))
    mrig.append(x)
print(mrig)

# Check the index of an array value
val=int(input('Enter value to search'))
print(mrig.index(val))



# Method	Description
# append()	Adds an element at the end of the list
# buffer_info()  Returns address and size of the array
# clear()	Removes all the elements from the list
# copy()	Returns a copy of the list
# count()	Returns the number of elements with the specified value
# extend()	Add the elements of a list (or any iterable), to the end of the current list
# index()	Returns the index of the first element with the specified value
# insert()	Adds an element at the specified position
# pop()	    Removes the element at the specified position
# remove()	Removes the first item with the specified value
# reverse()	Reverses the order of the list
# sort()	Sorts the list