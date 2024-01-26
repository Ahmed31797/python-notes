students = []
invalidChoice = 0
while True:
    print(""" 
        1. Add student
        2. List student
        3. Delete student
        4. Exit
    """)

    choice = int(input("Pick a number from the menu: "))
    if choice == 1:
        name = input("Enter student name: ").lower()
        students.append(name)
        print("Student Adedded")
    elif choice == 2:
        for st in students:
            print (st)
    elif choice == 3:
        name = input("Enter student name to delete: ").lower()
        students.remove(name)
        print("Student deleted")
    elif choice == 4:
        break
    else:
        print("Invalid choice")
        invalidChoice +=1
        if invalidChoice == 3:
            print("Ciyaarta meesha kala tag")
            break
