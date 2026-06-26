# Student Data Analysis Project

# Step 1: Store student data
students = [
    {"name": "Ali", "marks": 85},
    {"name": "Rahul", "marks": 78},
    {"name": "Sara", "marks": 92},
    {"name": "John", "marks": 67},
    {"name": "Ayesha", "marks": 74}
]

# Step 2: Calculate average marks
def calculate_average(data):
    total = 0
    for student in data:
        total += student["marks"]
    return total / len(data)

# Step 3: Find topper
def find_topper(data):
    topper = data[0]
    for student in data:
        if student["marks"] > topper["marks"]:
            topper = student
    return topper

# Step 4: Display results
average = calculate_average(students)
topper = find_topper(students)

print("Average Marks:", average)
print("Topper:", topper["name"], "-", topper["marks"])

# Step 5: Grade system
def assign_grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 75:
        return "B"
    elif marks >= 60:
        return "C"
    else:
        return "D"

print("\nStudent Grades:")
for student in students:
    grade = assign_grade(student["marks"])
    print(student["name"], "->", grade)