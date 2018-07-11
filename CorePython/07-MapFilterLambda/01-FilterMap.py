def tempConv(c):
    return 9/5 * c + 32

temp = [34.5,33.1,38.2,28.1,36.9]

f = list(map(tempConv, temp))
print(f)


def even(num):
    return num % 2 == 0

evenList = list(filter(even, [i for i in range(0,51)]))
print(evenList)
