def student_data_organizer():
    # Main storage lists and sets
    all_students = []
    all_subjects_offered = set()

    while True:
        print("\n=== Welcome to the Student Data Organizer! ===")
        print("1. Add Student")
        print("2. Display All Students")
        print("3. Update Student Information")
        print("4. Delete Student")
        print("5. Display Subjects Offered")
        print("6. Exit")
        
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input! Please enter a number between 1 and 6.")
            continue

        if choice == 1:
            print("\nEnter student details:")
            student_id = input("Student ID: ")
            name = input("Name: ")
            
            try:
                age = int(input("Age: "))
            except ValueError:
                age = 0  # Default or handling non-integer age safely
                
            grade = input("Grade: ")
            dob = input("Date of Birth (YYYY-MM-DD): ")
            
            # Using Tuple to store unchanging unique details (Student ID & Date of Birth)
            immutable_info = (student_id, dob)
            
            subjects_input = input("Subjects (comma-separated): ")
            # Processing subjects into a list and adding unique ones to the global set
            subjects_list = [sub.strip() for sub in subjects_input.split(",")]
            for sub in subjects_list:
                all_subjects_offered.add(sub)

            # Dictionary containing student details
            student_record = {
                "id": immutable_info[0],
                "dob": immutable_info[1],
                "name": name,
                "age": age,
                "grade": grade,
                "subjects": subjects_list
            }

            # Adding dictionary to the main list
            all_students.append(student_record)
            print("Student added successfully!")

        elif choice == 2:
            print("\n--- Display All Students ---")
            if not all_students:
                print("No student records found.")
            else:
                for student in all_students:
                    # Using f-strings formatting for clean presentation
                    subjects_str = ", ".join(student["subjects"])
                    print(f"Student ID: {student['id']} | Name: {student['name']} | Age: {student['age']} | Grade: {student['grade']} | Subjects: {subjects_str}")

        elif choice == 3:
            print("\n--- Update Student Information ---")
            target_id = input("Enter Student ID to update: ")
            found = False
            for student in all_students:
                if student["id"] == target_id:
                    found = True
                    print(f"Updating details for {student['name']}")
                    student["name"] = input("New Name: ")
                    try:
                        student["age"] = int(input("New Age: "))
                    except ValueError:
                        pass
                    student["grade"] = input("New Grade: ")
                    print("Student information updated successfully!")
                    break
            if not found:
                print("Student ID not found.")

        elif choice == 4:
            print("\n--- Delete Student ---")
            target_id = input("Enter Student ID to delete: ")
            found = False
            for i, student in enumerate(all_students):
                if student["id"] == target_id:
                    # Using the del keyword to delete a student record from the list
                    del all_students[i]
                    found = True
                    print(f"Student ID {target_id} deleted successfully!")
                    break
            if not found:
                print("Student ID not found.")

        elif choice == 5:
            print("\n--- Display Subjects Offered ---")
            if not all_subjects_offered:
                print("No subjects available yet.")
            else:
                print("Unique Subjects Offered:")
                for sub in all_subjects_offered:
                    print(f"- {sub}")

        elif choice == 6:
            print("\nThank you for using the Student Data Organizer. Goodbye!")
            break
        else:
            print("Invalid choice! Please choose between 1 and 6.")

# Run the program
if __name__ == "__main__":
    student_data_organizer()