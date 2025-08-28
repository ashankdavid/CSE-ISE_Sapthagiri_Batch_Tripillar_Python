# Find out the Max and Min element of the List without using any inbuilt function in python!

myList = [100, 5, 70, 42, 1, 24]

maxValue = myList[0]
minValue = myList[0]

for i in myList:
    if i > maxValue:
        maxValue = i
    if i < minValue:
        minValue = i

print(maxValue)
print(minValue)