# Definition: A set is an unordered, collection of data

# Properties
# Unordered
# Mutable
# Does not allow duplicate elements

mySet = {1,2,3,4,5,5}
print(mySet)

mySet.add(10)
print(mySet)

mySet.remove(2)
print(mySet)

mySet.pop()
print(mySet)

set_a = {1,2,3}
set_b = {3,4,5}

union = set_a | set_b
print(union)
intersection = set_a & set_b
print(intersection)
difference1 = set_a - set_b
print(difference1)
difference2 = set_b - set_a
print(difference2)