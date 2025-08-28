# Count how many times an element appears in  a list

myList = [1,2,3,4,2,6,3,7,4,7,1,2,1,4,5]
target = 1

count = 0

for i in myList:
    if i == target:
        count += 1

print(count)