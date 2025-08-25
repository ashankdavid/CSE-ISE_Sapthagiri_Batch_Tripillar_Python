rows = int(input('Enter the rows: '))
for i in range(rows):
    for spaces in range(rows-i-1):
        print(" ", end=' ')
    for stars in range(2*i+1):
        print("*", end=' ')
    print()