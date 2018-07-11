import time


startTime = time.time()


# eList = []
# oList = []
#
# for i in range(1,10000000):
#     if i % 2 == 0:
#         eList.append(i)
#     else:
#         oList.append(i)
# print(eList)
# print(oList)

evenList = [i for i in range(1,10000000) if i % 2 == 0]
oddList = [j for j in range(1,10000000) if j % 2 != 0]

# print(evenList)
# print(oddList)


endTime = time.time()
print("Total Time :",endTime - startTime)
