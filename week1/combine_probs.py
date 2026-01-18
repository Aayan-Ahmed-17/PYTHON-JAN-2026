"""
Q1.
Write a program that:
Keeps asking the user for numbers
Stops when the user enters 0
Prints the sum of all entered numbers
"""
total = 0
while True:
    u_num = input("Enter your num here: ")
    if not u_num.isdigit():
        print("Enter valid num")
        continue

    num = int(u_num)

    if num == 0:
        print(total)
        break
    
    total += num






