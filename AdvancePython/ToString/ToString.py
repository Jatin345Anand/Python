class Person:

    def __init__(self):
        self.name = 'Ram'
        self.age = 23
        self.company = 'HCL'

    # ToString - Convert object to human readable format
    def __str__(self):
        return self.name + str(self.age) + self.company

obj = Person()
print(obj)