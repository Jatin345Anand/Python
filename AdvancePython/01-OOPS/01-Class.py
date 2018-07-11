class Student:
    id = 0
    name = ""
    age = 0
    course = "btech"
    college = "IP"

print(__name__)

if __name__ == '__main__':
    ram = Student()
    # print(ram)
    ram.id = 1
    ram.name = "Ram"
    ram.age = 21

    shyam = Student()
    shyam.id = 2
    shyam.name = "Shyam"
    shyam.age = 24
