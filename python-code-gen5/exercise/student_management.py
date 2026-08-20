"""
This is student management system using with data structure (List, Tuple, Set)

Objective
- View Student
- Add Student
- Update Student
- Delete Student

"""

list_students = []

while True:
    def display():
        print("==" * 15)
        print("Welcome To Student Management")
        print("==" * 15)
        print("1. View Student")
        print("2. Add Student")
        print("3. Update Student")
        print("4. Delete Student")

        option = int(input("Enter Option (1-4): "))
        match option:
            case 1:
                view()
            case 2:
                add()
            case 3:
                update()
            case 4:
                delete()

    def view():
        if len(list_students) == 0:
            print("Student Not Found")
        print(list_students)

    def add():
        name = input("Enter Student Name: ")
        list_students.append(name)
        print("Student Added Successfully")

    def delete():
        name = input("Find Student Name: ")
        if name in list_students:
            list_students.remove(name)
            print("Student Deleted Successfully")

    def update():
        name = input("Find Student Name: ")
        if name in list_students:
            print("Student Exist")
            new_name = input("Enter New Name: ")
            list_students.remove(name)
            list_students.append(new_name)
            print("Student Updated Successfully")
        print("Student Not Found")
            

    display()