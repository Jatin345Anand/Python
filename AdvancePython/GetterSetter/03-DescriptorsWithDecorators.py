class Person:

    def __init__(self):
        self.__name = ""

    @property
    def name(self):
        print("Getting",self.__name)
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value
        print("Name is",self.__name)

obj = Person()
obj.name = 'Ram'
print(obj.name)