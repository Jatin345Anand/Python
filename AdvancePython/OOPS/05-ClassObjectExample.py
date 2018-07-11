import sys
import weakref

class Emp():
    """This is employee class"""

    def __init__(self,name,salary):
        self.name = name
        self.salary = salary

    def showEmp(self):
        return self.name, self.salary

# print(__name__)

if __name__ == '__main__':
    obj = Emp('Ram', 25000)
    # print(Emp.__name__)
    # print(Emp.__doc__)
    # print(Emp.__dict__)
    # print(obj.__class__)
    # obj.showEmp()
    print(obj.showEmp())
    print(sys.getsizeof(obj))
    # obj_2 = obj
    print(hex(id(obj)))
    ref = weakref.ref(obj)
    print("Before", ref)
    del obj
    print("After", ref)