with open('demo_1.txt', 'r') as file:
    # data = file.read()
    # print(len(data))
    # for i in range(100):
    #     print(file.readline(), end='')
    data = file.readlines()
    print(data)
