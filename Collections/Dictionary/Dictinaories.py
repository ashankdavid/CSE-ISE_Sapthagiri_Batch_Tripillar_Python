# Definition: it a type of collection in python which is mutable, unordered , with unique keys

#Properties
# Unordered (Python 3.7+, maintansthe order of insertion)
# Mutable
# Keys should be unique

# Operations

dict1 = {'name':'Ashank', 'EmpID':123, 'city':'Bengaluru'}
dict2 = {'name':'Abhishek', 'EmpID':456, 'city':'Kerla'}
dict3 = {'name':'David', 'EmpID':678, 'city':'Mangalore'}

print(dict1)
print(dict1['name'])

# Adding some values into Dictionary
dict1['job'] = 'Trainer'
print(dict1)
dict2['job'] = 'Student'
print(dict2)

# Removing a value from dictionary
#1 Pop()
#2 PopItem()
#3 del
#4 clear()

#1 Pop() - removes a particular element which u cant to remove
dict1.pop('city')
print(dict1)

#2 PopItem() - removes the latest entry from dict1
dict1.popitem()
print(dict1)

#3 del
del dict2['city']
print(dict2)

#4 clear()
dict3.clear()
print(dict3)

# Disctionry Functions
# 1) keys()
# 2) Values()
# 3) items()
# 4) get()
# 5) update()

myDict = {'name':"Ashank", 'EmpID':123, 'city':'Bengaluru'}
# 1) keys()
keys = myDict.keys()
print(type(keys))
print(keys)
for i in keys:
    print(i)

# 2) Values()
Values = myDict.values()
print(type(Values))
print(Values)
for i in Values:
    print(i)

# 3) items()
Items = myDict.items()
print(type(Items))
print(Items)
for i in Items:
    print(i)

# 4) get()
print(myDict.get('name'))
print(myDict.get('city'))

# 5) Update()
myDict.update({"city":"Mysore"})
print(myDict)

dictionary = {}
numItems = int(input("Enter the number of items: "))
for i in range(numItems):
    key = input("Enter a key: ")
    val = input("Enter a value: ")
    dictionary[key] = val

print(dictionary)