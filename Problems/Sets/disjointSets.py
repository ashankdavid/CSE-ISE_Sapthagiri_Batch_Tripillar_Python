def disjoint(a, b):
    for i in a:
        for j in b:
            if i==j:
                return False
    return True


set1 = {1,2,3}
set2 = {4,5}
set3 = {3,6}

print(disjoint(set1, set2)) # True
print(disjoint(set1, set3)) # False