while True:
    print(
        """ 
        1. Add a student
        2. Delete a student
        3. Exit
        """
    )

    ans = int(input("Choose a number from the menu: "))
    if ans == 1:
        print(
        """ 
        1. Male
        2. Female
        """
        )
        gender = int(input("Gender: "))
        student_name = input("Enter a name: ")
        age = int(input("Age: "))
        if age < 18:
            print("You are underage. Bye bye.")
            break
        if gender == 1:
            print("Mr. " + student_name + " added.")
        elif gender == 2:
            print("Mrs. " + student_name + " added.")
        else:
            print("No gender as such.")
    elif ans == 2:
        student_name = input("Enter a name to delete: ")
        print(student_name + " deleted.")
    elif ans == 3:
        print("Goodbye")
        break
    else:
        print("invalid number")
        
