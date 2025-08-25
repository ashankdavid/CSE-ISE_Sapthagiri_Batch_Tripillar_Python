n = int(input("Enter a num: "))
n1 = 0
n2 = 1
sum = 0

print(n1, n2, end =" ")
for i in range(2, n):
    sum = n1 + n2
    print(sum, end = " ")
    n1 = n2
    n2 = sum