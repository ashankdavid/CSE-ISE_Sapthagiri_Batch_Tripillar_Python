# Definition: A tuple is a ordered, immutable, collection of items, it also allows duplicates elements in it

# Properties
# Ordered
# Immutable
# Allows Duplicate elements

myTuple = (1,"Sapthagiri", True, 1.5, 2, 3, 4, 5,"Sapthagiri")
# It allows Hetrogenuos data as it is dynamically typed

anotherTuple = tuple(range(10))

# Accessing Elements
print(myTuple[0])
print(myTuple[3])
print(myTuple[-2])

# Operations on Tuples
# 1) Concatenation of 2 tuples
tuple1 = (1,2,3)
tuple2 = (4,5,6)
resultTuple = tuple1 + tuple2
print(resultTuple)

# 2) Repeatations of a tuples
originalTuple = (1,2,3,4,5)
repeatedTuple = originalTuple * 3
print(repeatedTuple)

# 3) Membership of element in a tuple
sampleTuple = (1,2,3,4,5,6)
print(3 in sampleTuple)
print(10 in sampleTuple)
print(3 not in sampleTuple)
print(10 not in sampleTuple)

# Length of the tuple
Length = len((1,2,3,4,5))
print(Length)

# 1st inbuilt tuple function - index function
index = myTuple.index(1.5)
print(index)

# 2nd invuilt tuple function - count
count = myTuple.count("Sapthagiri")
print(count)

# Notes
# There are only 2 inbuilt tuple functions - index and count
# Why? - tuples are immutable!, they cannot be modified
# sooo we have very limited options with tuples

# Once the tuple is created then u cannot change it
# this is Tuple!

# Bonus Concept!!! - IMPORTANT - TUPLE UNPACKING!!!
# Tuple unpacking, assigning the values from a tuple to various different variables in one single line!
nums1 = (1,2,3)
a,b,c = nums1
print("After Unpacking 1!")
print(a)
print(b)
print(c)

nums2 = (4,5,6)
i,_,k = nums2 # Here _ is a dummy variable
print("After Unpacking 2!")
print(i)
print(k)

nums3 = (1,2,3,4,5,6,7,8,9,10)
a,b,c,*rest = nums3
print(a)
print(b)
print(c)
print(rest)

# Swapping two numbers using tuple unpacking!
x = 5
y = 10

print(f"Before swapping x = {x}, y = {y}")
x, y = y, x
print(f"Before swapping x = {x}, y = {y}")

