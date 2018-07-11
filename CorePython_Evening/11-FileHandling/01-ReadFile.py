# file = open('C:/Users/asus/Desktop/demo.txt', 'r')

# By default - it open the file in read mode
file = open('demo.txt')

data = file.read()

print(data)

file.close()
