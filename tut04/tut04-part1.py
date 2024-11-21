# Initialize the student grades dictionary
students = {}

# Function to add a new student
def add_student(name, grades):
    name = name.lower()  # Convert name to lowercase
    if name not in students:
        students[name] = grades
    else:
        print(f"Student '{name}' already exists. Use update function to modify grades.")

# Function to update grades of an existing student
def update_grades(name, grades):
    name = name.lower()  # Convert name to lowercase
    if name in students:
        students[name] = grades
    else:
        print(f"Student '{name}' does not exist. Use add function to add the student.")

# Function to calculate the average grade of a student
def calculate_average(grades):
    total = 0
    for grade in grades:
        total += grade
    return total / len(grades)

# Function to print all students with their average grades
def print_students_with_averages():
    print("\nStudents and their Average Grades:")
    for name, grades in students.items():
        avg = calculate_average(grades)
        print(f"{name.capitalize()} - Average: {avg:.2f}")

# Function to sort students by their grades in descending order
def sort_students_by_average():
    sorted_students = []
    for name, grades in students.items():
        avg = calculate_average(grades)
        inserted = False
        for i in range(len(sorted_students)):
            if avg > sorted_students[i][1]:
                sorted_students.insert(i, (name, avg))
                inserted = True
                break
        if not inserted:
            sorted_students.append((name, avg))
    return sorted_students

# Sample Interaction
add_student("Anmol", [85, 90, 88])
add_student("Naresh", [78, 81, 85])
add_student("Neha", [92, 87, 90])
update_grades("naresh", [80, 82, 84])

print_students_with_averages()

sorted_students = sort_students_by_average()
print("\nStudents sorted by Average Grade (Descending):")
for name, avg in sorted_students:
    print(f"{name.capitalize()} - Average: {avg:.2f}")
