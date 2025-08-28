# Rotate a list by K steps
# example - [1,2,3,4,5] --> [4,5,1,2,3], if k = 2

def rotateByK(list, k):
    n = len(myList)
    k = k % n
    return myList[-k:] + myList[:-k]

myList = [1,2,3,4,5]
k = 5
rotatedList = rotateByK(myList, k)
print(rotatedList)
