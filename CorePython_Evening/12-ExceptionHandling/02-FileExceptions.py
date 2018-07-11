try:
    file = open('demo.txt')
    data = file.read()
    print(data)
except FileNotFoundError as err:
    print(err)
finally:
    file.close()
