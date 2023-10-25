#list methods

numbers = [1,2,3,4,5]
numbers.append(6) #inserting number at the end of the list
print(numbers)

numbers.insert(0,0) # index: int and object T
print(numbers)

numbers.remove(3) #remove the given element from list
print(numbers)

numbers.clear() #clear the entire list
print(numbers)

#Boolean expression for checking lists
print(1 in numbers)

numbers.insert(0,1) # adding 1 to list
print(numbers)
print(1 in numbers)

#Len returns the number of elements in a list
numbers = [1,2,3,4,5]
print(len(numbers))

print("***********************************************************")
#FOR LOOPS
numbers = [1,2,3,4,5]

for x in numbers:
    print(x)
    
print("***********************************************************")
#range()

nums = range(5) # range object is an object that can store a sequence of numbers
print(nums)

for x in nums:
    print(x)
print("done")
    
nums = range(5,10)
for x in nums:
    print(x)
print("done")

nums = range(5, 10, 2) # first two numbers are the range and the last number is the step. 2 means it will skip a number.(5-7-9)
for x in nums:
    print(x)
print("done")

print("***********************************************************")
#tuples They are like list but you cant change them
tup = (1,2,3)

print(tup.count(2)) # return the number of occurance of that element
print(tup.index(3)) # returns the index of the first occurance of the element

