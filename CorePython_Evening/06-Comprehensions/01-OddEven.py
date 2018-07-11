def even(x):
    return x%2 == 0

def odd(x):
    return x %2 != 0

evenList = []
oddList = []

evenList.append(list(filter(even, range(1,101))))
oddList.append(list(filter(odd, range(1,101))))

print("Even list :",evenList)
print("Odd list :",oddList)
