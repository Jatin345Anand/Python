class Person():
    def __init__(self):
        self.id = 0
        self.name = None
        self.age = 0

    def printPerson(self):
        print("Person Details",self.id, self.name, self.age)

class Emp(Person):
    def __init__(self):
        self.id = 101
        self.name = "Ram"
        self.age = 25
        self.company = "HCL"

    def printEmp(self):
        print("Company is",self.company)

class Student(Person):
    def __init__(self):
        self.id = 102
        self.name = "Shyam"
        self.age = 16
        self.college = "IP"

    def printStudent(self):
        print("Student college is",self.college)


emp = Emp()
emp.printPerson()
emp.printEmp()
student = Student()
student.printPerson()
student.printStudent()