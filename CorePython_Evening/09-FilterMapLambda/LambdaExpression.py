def tempConv(c):
    return 9/5 * c + 32

cel = [32.3,34.5,36.1,38.2,26.7,29.8]

fah = list(map(tempConv, cel))
print(fah)


fah_1 = list(map(lambda x: 9/5 * x + 32, cel))
print(fah_1)

evenList = list(filter(lambda x : x % 2 == 0, [i for i in range(1,101)] ))
print(evenList)
