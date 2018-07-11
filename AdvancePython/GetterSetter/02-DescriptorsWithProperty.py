class Person:

    def __init__(self):
        self.__name = ''

    def fset(self, value):
        self.__name = value
        print("Value set for",self.__name)

    def fget(self):
        return self.__name

    def fdel(self):
        print("Deleting",self.__name)

    username = property(fget, fset, fdel)

obj = Person()
obj.username = 'Ram'
print(obj.username)
del obj.username