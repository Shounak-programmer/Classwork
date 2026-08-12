#Create a menu-driven program using functions and a dictionary to add a student, update marks, search for a student, display the topper, and display the average marks.
def add(stu):
    name = input("Enter student name: ")
    if name in stu:
        print(f"Student {name} already exists. Use update option to change marks.")
        return
    marks = float(input("Enter student marks: "))
    stu[name] = marks
    print(f"Student {name} added successfully.")
def upd(stu):
    name = input("Enter student name to update marks: ")
    if name in stu:
        marks = float(input("Enter new marks: "))
        stu[name] = marks
        print(f"Marks for {name} updated successfully.")
    else:
        print(f"Student {name} not found.")
def srch(stu):
    name = input("Enter student name to search: ")
    if name in stu:
        print(f"Student {name} has marks: {stu[name]}")
    else:
        print(f"Student {name} not found.")
def top(stu):
    if stu:
        topper = max(stu, key=stu.get)   #.get is used to get the value of the key (marks) for comparison
        print(f"The topper is {topper} with marks: {stu[topper]}")
    else:
        print("No student found.")
def avg(stu):
    if stu:
        average = sum(stu.values()) / len(stu)
        print(f"The average marks of the class is: {average:.2f}")
    else:
        print("No student found.")

print("Welcome to the Student Management System")
stu = {}
invalid_limit = 3
invalid_count = 0
a = input("Enter your choice (add/update/search/topper/average/exit): ").lower().strip()
while a != "exit":
    if a == "add":
        add(stu)
    elif a == "update":
        upd(stu)
    elif a == "search":
        srch(stu)
    elif a == "topper":
        top(stu)
    elif a == "average":
        avg(stu)
    else:
        print("Invalid choice. Please try again.")
        invalid_count += 1
    if invalid_count >= invalid_limit:
        print("Too many invalid attempts. Exiting the program.")
        break
    
    a = input("Enter your choice (add/update/search/topper/average/exit): ").lower().strip()