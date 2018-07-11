class Emp():

    def __init__(self,name,age,salary,address):
        self.name = name
        self.age = age
        # Protected
        self._salary = salary
        # Private
        self.__address = address

    def printEmp(self):
        print(self.name,self.age)
        print("Salary of {} is {}".format(self.name, self._salary))
        print("Address of {} is {}".format(self.name,self.__address))

obj_1 = Emp('Ram', 23,22000,'xyz')
obj_1.name = 'Ajay'
obj_1._salary = 12000
# obj_1.__address = 'Delhi'
obj_1.printEmp()

obj_2 = Emp('Shyam',28,25000,'abc')
obj_2.printEmp()