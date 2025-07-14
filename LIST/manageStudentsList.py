# Initialize an empty list for student names
students = []

while True:
    print("\nOptions:")
    print("1. Add a student")
    print("2. Remove a student")
    print("3. Display all students")
    print("4. Sort students")
    print("5. Exit")

    choice = input("Choose an option (1-5): ")

    if choice == '1':
        name = input("Enter the name of the student to add: ")
        students.append(name)
        print(f"{name} has been added to the list.")

    elif choice == '2':
        name = input("Enter the name of the student to remove: ")
        if name in students:
            students.remove(name)
            print(f"{name} has been removed from the list.")
        else:
            print(f"{name} is not in the list.")

    elif choice == '3':
        print("Current list of students:")
        for student in students:
            print(student)

    elif choice == '4':
        students.sort()
        print("Students have been sorted.")

    elif choice == '5':
        print("Exiting the program.")
        break

    else:
        print("Invalid option, please try again.")
