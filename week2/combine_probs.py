# Q6. Student Records
# Tasks:
# Print each student’s name
# Print their average marks
# Find the student with the highest average
students = [
    ("Ali", [78, 85, 90]),
    ("Sara", [88, 92, 79]),
    ("Ahmed", [70, 65, 80])
]

highest_avg = 0
top_student = ""

for name, marks in students:
    avg = sum(marks) / len(marks)
    print(f"{name} average marks are : {avg}")

    if avg > highest_avg:
        highest_avg = avg
        top_student = name

print("Top student:", top_student)

