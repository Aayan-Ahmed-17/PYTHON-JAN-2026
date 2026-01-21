# 1. Lists
# Q1. Student Marks

# marks = [45, 78, 90, 32, 67, 88]
# Tasks:
# Print all marks
# Add a new mark 76
# Remove the lowest mark
# Print the final list

marks = [45, 78, 90, 32, 67, 88]

print(marks)
marks.append(76)

marks.remove(min(marks))

print(marks)

