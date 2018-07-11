class Emp():
    # id = 1
    # name = "Ram"
    # age = 25

    def showEmp(this,id,name,age,salary):
        # print("ID {}, Name {} and Age {}".format(Emp.id,Emp.name,Emp.age))
        print("ID {}, Name {} and Age {}".format(id, name, age))
        print("Salary of {} is {}".format(name,salary))

ram = Emp()
ram.address = 'xyz'
ram.showEmp(101,'Ram',25,25000)
print("Address of Ram",ram.address)

shyam = Emp()
shyam.showEmp(102,'Shyam',26,28000)