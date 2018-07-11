studentList = []

students = {}

def create():
    print("Create Student Record...")
    studentId = int(input("Enter ID : "))
    studentName = input("Enter name : ")
    studentCourse = input("Enter course : ")
    studentNo = int(input("Enter number : "))

    students["Id"] = studentId
    students["Name"] = studentName
    students["Course"] = studentCourse
    students["No"] = studentNo

    # studentList.append([studentId, studentName, studentCourse, studentNo])
    studentList.append(students.copy())
    for s in studentList:
        print(s)

def read():
    print("Read Student Record...")
    for s in studentList:
        print(s)

# def searchStudent():
#     choice = input("Search student by ID or Name ? ")
#     if choice.lower() == 'id':
#         studentId = int(input("Enter Student ID you want to search : "))
#         for student in studentList:
#             if student['Id'] == studentId:
#                 print("Student Exist")
#                 print("Search Result : ",student['Name'], student['Course'])
#             else:
#                 print("Student do not exist")
#     elif choice.lower() == 'name':
#         studentName = input("Enter Student Name you want to search : ")
#         for student in studentList:
#             if student['Name'].lower() == studentName.lower():
#                 print("Student Exist")
#                 print("Search Result : ",student['Id'],student['Name'], student['Course'])
#             else:
#                 print("Student do not exist")

def searchStudent():
    choice = input("Search student by ID or Name ? ")
    studentVal = input("Enter {} of student".format(choice))
    searchResult = list(filter(lambda x : x[choice] == studentVal, studentList))
    print(searchResult)

def update():
    print("Update Student Record...")

def delete():
    print("Delete Student Record...")
    studentId = int(input("Enter Student ID you want to delete : "))
    for i in range(len(studentList)):
        if studentList[i]['Id'] == studentId:
            print("Student Exist")
            del studentList[studentId - 1]
            print("Deleted Successfully...")
            print("Updated List...")
            read()
        else:
            pass
            # print("Student do not exist")

def sortStudents():
    sortedList = sorted(studentList, key=lambda x : x["Name"])
    for s in sortedList:
        print(s)

def save():
    with open("students.txt", "a") as file:
        # file.write(str(studentList))
        for data in studentList:
            formattedData = str(data).strip("{}")
            file.write(formattedData + "\n")

while True:
    print("""
    1. Create Record
    2. Read Record
    3. Update Record
    4. Delete Record
    5. Search Record
    6. Sort Record
    7. Save Record
    8. Load Record
    9. Quit
    """)

    todo = {
        "1" : create,
        "2" : read,
        "3" : update,
        "4" : delete,
        "5" : searchStudent,
        "6" : sortStudents,
        "7" : save,
        "9" : quit
    }

    userChoice = input("Enter your choice : ")

    todo.get(userChoice)()
