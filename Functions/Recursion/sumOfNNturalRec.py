def sumN(n):
    if n==1:
        return 1
    return n * sumN(n-1)

num = int(input("Enter a number: "))
print(sumN(num))