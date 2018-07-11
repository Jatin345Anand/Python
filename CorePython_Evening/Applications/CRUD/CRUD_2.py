empList = []
empData = {}
def addEmp():
    emp_name = input("Enter name of Emp : ")
    emp_age = int(input("Enter age of Emp : "))
    emp_sal = int(input("Enter salary of Emp : "))

    empData["name"] = emp_name
    empData["age"] = emp_age
    empData["salary"] = emp_sal

    empList.append(empData.copy())
    print("Data Added Successfully...")
    for index,d in enumerate(empList):
        print(index+1,d)

def readEmp():
    for index,d in enumerate(empList):
        print(index+1,d)

def updateEmp():
    toUpdate = int(input("Enter id of Emp you want to update : "))
    print("You want to update: \n")
    print(empList[toUpdate-1])

    userFeature = input("What do you want to update : Name, age or salary : ")

    if userFeature.lower() == "name":
        updatedName = input("Enter updated name of Emp : ")
        empList[toUpdate-1]["name"] = updatedName
        print("Data Updated Successfully...")
        readEmp()
    elif userFeature.lower() == "age":
        updatedAge = int(input("Enter updated age of Emp : "))
        empList[toUpdate-1]["age"] = updatedAge
        print("Data Updated Successfully...")
        readEmp()
    elif userFeature.lower() == "salary":
        updatedSalary = int(input("Enter updated age of Emp : "))
        empList[toUpdate-1]["salary"] = updatedSalary
        print("Data Updated Successfully...")
        readEmp()
    else:
        print("Wrong Choice...")



def deleteEmp():
    emp_to_delete = int(input("Enter id of Emp you want to delete : "))
    del empList[emp_to_delete - 1]
    print("Deleted Successfully...")
    print("Updated List...")
    for index,d in enumerate(empList):
        print(index+1,d)

def saveEmp():
    with open('data.txt', 'a') as file:
        # file.write(str(empList).strip('[]') + "\n")
        for data in empList:
            file.write(str(data).strip('{}') + "\n")
    print("Data Written successfully...")

def loadEmp():
    pass

def errHandler():
    print("Wrong Choice.....")


while True:

    print("""
    1. Add Emp
    2. Read Emp
    3. Update Emp
    4. Delete Emp
    5. Search Emp
    6. Sort Emp
    7. Save Emp
    8. Load Emp
    9. QUIT
    """)

    todo = {
        "1" : addEmp,
        "2" : readEmp,
        "3" : updateEmp,
        "4" : deleteEmp,
        "7" : saveEmp,
        "9" : quit
    }

    user_choice = input("Enter your choice : ")
    todo.get(user_choice, errHandler)()
