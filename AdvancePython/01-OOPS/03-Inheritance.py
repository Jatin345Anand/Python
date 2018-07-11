class Human:

    def __init__(self, name, age, country, occupation):
        self.name = name
        self.age = age
        self.country = country
        self.occupation = occupation

    def printHuman(self):
        print(self.name, self.age, self.country, self.occupation)

class Employee(Human):

    def __init__(self,name, age, country, occupation, salary, bank):
        self.salary = salary
        self.bank = bank
        self.name = name
        self.age = age
        self.country = country
        self.occupation = occupation
        super().__init__(self.name, self.age, self.country, self.occupation)

    def printEmp(self):
        print(self.salary, self.bank)

class Student(Human):

    def __init__(self,name, age, country, occupation, grade, school):
        self.grade = grade
        self.school = school
        self.name = name
        self.age = age
        self.country = country
        self.occupation = occupation
        super().__init__(self.name, self.age, self.country, self.occupation)

    def printStudent(self):
        print(self.grade, self.school)

emp = Employee("Ram", 21, "India", "SD", 23000, "HDFC")
emp.printHuman()
emp.printEmp()

stud_1 = Student("Shyam", 15, "India", "Student", 8, "DPS")
stud_1.printHuman()
stud_1.printStudent()
