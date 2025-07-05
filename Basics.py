print (2+2)
operator=input('Please provide the operator')
A=int (input('Please provide the first input'))
B=int (input('Please provide the second input'))

if operator=='+':
    print (A+B)
elif operator=='-':
    print (A-B)
elif operator=='*':
    print (A*B)
elif operator=='/':
    print (A/B)
else:
    print ('Invalid Input')

arr=[1,2,3,4]  #An array is a special variable, which can hold more than one value at a time. Array is a collection of items stored at contiguous memory locations. Array can only store one data type say 'int' or 'str'
list=[1,2,"Mriganka","Dharitri",7,9]  #List a data structure that can hold more than one value at a time; It is more flexible than array because it can store multiple data types; the items are ordered and can be changed i.e. they are mutable
dict={'key1':26,'key2':24,'key3':30}  #a dictionary is a data structure that stores data as key-value pairs
tup=(1,2,3,4)  #Tuple a data structure that can hold more than one value at a time; the items are ordered and cannot be changed i.e. they are immutable

print (type(tup))
print (type(dict))
print (type(list))

print (arr[2]+arr[3])

print (dict['key3']+dict['key2'])
arr.append(7)
print (arr)

print((2+3) == (2+2)) #Identity Operator

print(3 in [1,3,4,5]) #Membership Operator

print (('1') and ('1'))