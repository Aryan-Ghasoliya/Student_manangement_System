
students = []

def add_student():
    student_id = input("Enter Student ID: ")
    name = input("Enter Student Name: ")
    age = int(input("Enter Student Age: "))
    course = input("Enter Course: ")

    student = {
        "id": student_id,
        "name": name,
        "age": age,
        "course": course
    }

    students.append(student)
    print("Student added successfully!")


def view_students():
    if not students:
        print("No students found.")
        return

    for student in students:
        print(student)


def main():
    while True:
        print("\n--- Student Management System ---")
        print("1. Add Student")
        print("2. View Students")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            break
        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()


"New information is being sent"
# Student Management System
print("Welcome to Student Management System")
print("wwwwwwwwwwwwwwwwwwwwwwww")


students = []

def add_student():
    print("\n--- Add New Student ---")

    student_id = input("Enter Student ID: ")
    name = input("Enter Student Name: ")
    age = int(input("Enter Student Age: "))
    course = input("Enter Course: ")

    student = {
        "id": student_id,
        "name": name,
        "age": age,
        "course": course
    }

    students.append(student)

    print("\nStudent added successfully!")
    print("Student Details:", student)


def main():
    while True:
        print("\n--- Student Management System ---")
        print("1. Add Student")
        print("2. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            print("Exiting application...")
            break
        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()


print("Somwthing new is happing")
print("whaowahowaho")


def view_students():
    print("\n========== STUDENT RECORDS ==========")

    if not students:
        print("No student records found.")
        return

    for student in students:
        print("--------------------------------")
        print(f"Student ID   : {student['id']}")
        print(f"Student Name : {student['name']}")
        print(f"Age          : {student['age']}")
        print(f"Course       : {student['course']}")

    print("--------------------------------")
    print(f"Total Students: {len(students)}")


print("somewhere out of no where")
print("why he is here what am i doing")
