"""Q1) Print numbers from 1 to 20, but:
Skip numbers divisible by 3"""

# for num in range(1, 20):
#     if num % 3 == 0:
#         continue

#     print(num)
"""
Q2.) Print the table of a number entered by the user (up to 10).
"""
# u_num = int(input("Enter your number: "))
# for i in range(1, 11):
#     print(f"{u_num} x {i} = {u_num * i}")
#     i+=1

"""
Q3.) Ask the user for a number and:
Calculate the sum of digits
Example: 123 → 6
"""
# u_input = input("Enter your number: ")
# total = 0

# for digit in u_input:
#     total += int(digit)

# print(total)


# while True:
#     u_input = input("Enter your number: ")

#     if u_input.lower() == "end":
#         break

#     total = 0
#     for digit in u_input:
#         total += int(digit)

#     print(total)

# print("end")


"""
print this pattern
*
**
***
****
*****
"""
char = input("Enter any single character here: ")

if char:
    for i in range(1, 6):
        print(char[0] * i)
else:
    print("can't be empty")

