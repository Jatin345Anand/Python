class Emp():
    # Class Variables
    id = 0
    name = None
    age = 0

    print(id,name,age)


Emp.id = 1
Emp.name = 'Shyam'
Emp.age = 25

# print(Emp())
ram = Emp()
print(type(ram))
ram.id = 10
ram.age = 25
ram.name = 'Ram'

# Instance Variable
ram.salary = 25000
print(ram.id, ram.name, ram.age,ram.salary)

shyam = Emp()
print(shyam.id,shyam.name,shyam.age)