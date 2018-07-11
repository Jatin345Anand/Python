empList = []
def addEmp():
    emp_name = input("Enter name of Emp : ")
    emp_age = int(input("Enter age of Emp : "))
    emp_sal = int(input("Enter salary of Emp : "))
    data = [emp_name, emp_age, emp_sal]
    empList.append(data)
    print("Data Added Successfully...")
    for index,d in enumerate(empList):
        print(index+1,d)

def readEmp():
    for index,d in enumerate(empList):
        print(index+1,d)

def updateEmp():
    pass

def deleteEmp():
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
        "9" : quit
    }

    user_choice = input("Enter your choice : ")
    todo.get(user_choice, errHandler)()
