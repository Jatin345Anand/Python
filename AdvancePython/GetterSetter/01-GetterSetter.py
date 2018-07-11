class Person:

    # Magic Methods
    # Dunder Methods - Double Underscore
    def __init__(self):
        self.__name = ""

    def __set__(self, instance, value):
        self.__name = value
        print("Username",self.__name)
        # print(instance, value)

    def __get__(self, instance, owner):
        return self.__name
        # print(instance,owner)


class User():
    userName = Person()

obj = User()
obj.userName = 'Ram'
print(obj.userName)