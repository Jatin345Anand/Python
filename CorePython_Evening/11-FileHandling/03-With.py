# file = open('demo.txt')
# file.read()
# file.close

with open('demo.txt') as file:
    data = file.read()
    print(data)
