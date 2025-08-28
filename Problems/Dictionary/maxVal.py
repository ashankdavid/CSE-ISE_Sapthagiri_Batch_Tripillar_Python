marks = {'mark1':85, 'mark2':78, 'mark3':95}
highestKey = None
highestVal = float('-inf')
for k, v in marks.items():
    if v > highestVal:
        highestVal = v
        highestKey = k

print(highestKey)
print(highestVal)