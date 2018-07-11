a = 21

for i in range(2,a):
    if a%i == 0:
        print("{} is not a Prime number".format(a))
        break
else:
    print("{} is a Prime number".format(a))
