##num = 17
##
##for i in range(2,17):
##    if num % i == 0:
##        print("Not Prime")
##        break
##else:
##    print("Prime number...")


for i in range(100,500):
    for j in range(2,i):
        if i % j == 0:
            break
    else:
        print("{} is a Prime number".format(i))
