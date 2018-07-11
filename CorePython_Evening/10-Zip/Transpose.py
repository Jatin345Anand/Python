import numpy
a = [[1,2,3],
     [4,5,6],
     [7,8,9]]

z = zip(*a)

for i in z:
    print(i)

print(numpy.transpose(a))
