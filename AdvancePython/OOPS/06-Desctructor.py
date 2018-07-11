import sys
import weakref

class Emp():
    """This is employee class"""
    # Dunder Methods - Double Under Methods
    # Magic Methods
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary

    def showEmp(self):
        return self.name, self.salary

    # Destructor
    def __del__(self):
        print("Object Deleted...")

# print(__name__)

if __name__ == '__main__':
    obj = Emp('Ram', 25000)
    print(obj.showEmp())