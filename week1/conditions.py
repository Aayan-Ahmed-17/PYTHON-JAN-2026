# questions

"""
Q1) Take a user’s age and:
Print "Child" if age < 13
"Teenager" if age is between 13–19
"Adult" if age ≥ 20
"""
# u_age = int(input("Enter your age: "))

# if u_age < 13:
#     print("Child")
# elif 13 < u_age < 19:
#     print("Teenager")
# else:
#     print("Adult")

"""
Q2) Ask the user for a number and check whether it is:
Divisible by 3
Divisible by 5
Divisible by both
Or neither
"""

# u_num = int(input("Enter number: "))
# divisible_by_3 = not u_num % 3
# divisible_by_5 = not u_num % 5

# if divisible_by_3 and divisible_by_5:
#     print("both")
# elif divisible_by_3:
#     print("divisible by 3")
# elif divisible_by_5:
#     print("divisible by 5")
# else:
#     print("neither")

"""
Q3. Take three numbers and print the largest one.
"""

a = int(input("Enter number: "))
b = int(input("Enter number: "))
c = int(input("Enter number: "))

if a >= b and a >= c:
    print(a)
elif b >= c:
    print(b)
else:
    print(c)
