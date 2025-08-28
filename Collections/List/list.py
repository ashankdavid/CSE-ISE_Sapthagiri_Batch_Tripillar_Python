# Defination : A list is an ordered, mutable, collection of items

# Properties:
# Ordered
# Mutable
# Allows Duplicates

# Lists are dynamically typed and can store hetrogeneous data
list1 = [1,'Sapthagiri', True, 4.5]

myList = [1,2,3,4,5]
anotherList = list(range(2, 101, 2))

# Operations on List
# 1) Accessing elements from list
print(myList)
print(f"on 3rd index value is {myList[3]}")
print(f"on 0th index value is {myList[0]}")
# print(f"on 10th index value is {myList[10]}") #Error - Index Error
print(anotherList)
print(myList[2:4]) # Slicing of a List
print(anotherList[5:11])
print(myList[:4]) # Slice start - beginning
print(myList[3:]) # Slice stop - last
print(myList[:])
print(myList[-1:-5])

# 2) Modifying a list
print(myList)
myList[2] = 300
print(myList)

# 3) Printing the list

print(myList)
print(type(myList))

for i in myList:
    print(i, end=" ")
print()

# 4) Append

myList.append(6)
myList.append(7)
print(myList)
for i in range(8, 11):
    myList.append(i)

print(myList)

# 5) insert

myList.insert(6, 5000)
myList.insert(3, 'Sapthagiri')
print(myList)

# 6) Removing Element from list

myList.remove(5000)
print(myList)
myList.pop()
print(myList)
del myList[3]
print(myList)

# 7) Misc Functions
print(len(myList))
myList.sort()
print(myList)
myList.sort(reverse=True)
print(myList)