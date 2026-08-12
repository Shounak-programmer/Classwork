# Question 1:

# Write a Python program to store the name, marks in three subjects, and attendance percentage of multiple students using a nested dictionary.

# The program should:

# 1. Accept details of n students.

# 2. Calculate the total marks and average marks of each student.

# 3. Assign a grade based on the average:

# o 90–100 → A+

# o 80–89 → A

# o 70–79 → B

# o 60–69 → C

# o Below 60 → D

# 4. Display the complete details of all students.

# 5. Find and display the class topper.

# 6. Display the students whose attendance is below 75%.
def grade(avg):
    if avg >= 90:
        return "A+"
    elif avg >= 80:
        return "A"
    elif avg >= 70:
        return "B"
    elif avg >= 60:
        return "C"
    else:
        return "D"


def add_student(students):
    name = input("Enter student name: ")

    marks1 = float(input("Enter marks in Subject 1: "))
    marks2 = float(input("Enter marks in Subject 2: "))
    marks3 = float(input("Enter marks in Subject 3: "))
    attendance = float(input("Enter attendance percentage: "))

    total = marks1 + marks2 + marks3
    average = total / 3
    student_grade = grade(average)

    students[name] = {
        "marks": {
            "Subject 1": marks1,
            "Subject 2": marks2,
            "Subject 3": marks3
        },
        "attendance": attendance,
        "total": total,
        "average": average,
        "grade": student_grade
    }

    print("Student added successfully.")


def display_students(students):
    if not students:
        print("No students found.")
        return

    for name, details in students.items():
        print("\nName:", name)
        print("Subject 1:", details["marks"]["Subject 1"])
        print("Subject 2:", details["marks"]["Subject 2"])
        print("Subject 3:", details["marks"]["Subject 3"])
        print("Attendance:", details["attendance"], "%")
        print("Total:", details["total"])
        print("Average:", f"{details['average']:.2f}")
        print("Grade:", details["grade"])


def find_topper(students):
    if not students:
        print("No students found.")
        return

    topper = max(students, key=lambda name: students[name]["average"])

    print("\nClass Topper:", topper)
    print("Average:", f"{students[topper]['average']:.2f}")


def display_low_attendance(students):
    found = False

    print("\nStudents with attendance below 75%:")

    for name, details in students.items():
        if details["attendance"] < 75:
            print(name, "-", details["attendance"], "%")
            found = True

    if not found:
        print("No student has attendance below 75%.")


students = {}

while True:
    print("\n--- Student Management System ---")
    print("1. Add Student")
    print("2. Display All Students")
    print("3. Find Class Topper")
    print("4. Display Students Below 75% Attendance")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student(students)

    elif choice == "2":
        display_students(students)

    elif choice == "3":
        find_topper(students)

    elif choice == "4":
        display_low_attendance(students)

    elif choice == "5":
        print("Program exited.")
        break

    else:
        print("Invalid choice.")
