"""
Q1.
Write a program that:
Keeps asking the user for numbers
Stops when the user enters 0
Prints the sum of all entered numbers
"""
# total = 0
# while True:
#     u_num = input("Enter your num here: ")
#     if not u_num.isdigit():
#         print("Enter valid num")
#         continue

#     num = int(u_num)

#     if num == 0:
#         print(total)
#         break

#     total += num

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

while True:
    print("\n--- Calculator Menu ---")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    u_input = input("Enter your choice: ")
    num_1 = input("Enter first num: ")
    num_2 = input("Enter second num: ")

    if not u_input.isdigit() or not (0 < int(u_input) <= 5):
        print("please enter valid num 1-5")
        continue

    if not num_1.isdigit() or not num_2.isdigit():
        print("Enter valid nums")
        continue

    opr = int(u_input)
    int_1 = int(num_1)
    int_2 = int(num_2)

    match (opr):
        case (1):
            print(add(int_1, int_2))
        case (2):
            print(subtract(int_1, int_2))
        case (3):
            print(multiply(int_1, int_2))
        case (4):
            print(divide(int_1, int_2))
        case (5):
            break
        




