# Please write a function named seven_brothers. When the function is called, it should print out the names of the seven brothers in alphabetical order
def seven_brothers():
    names = ["Aapo", "Juhani", "Lauri", "Simeoni", "Timo", "Tuomas", "Eero"]
    names.sort()
    for name in names:
        print(name)


# Call the function to see the output
# ? seven_brothers()


# * AI Examples
# Function without parameters and return
def greet():
    print("This is my first function!")


# ? greet()


# Function with parameters
def greet_person(name, age):
    print(f"Hello {name}!")
    print(f"You are {age} years old.")


# ? greet_person("Aayan Ahmed", 19)
# ? greet_person("Annas Ahmed", 23)


# Function with parameter and return value
def calculate_area(length, width):
    area = length * width
    return area


# Call and store the result
room1_area = calculate_area(14, 9)
room2_area = calculate_area(8, 10)

# ? print(room1_area)
# ? print(room2_area)


# * Question 1: Temperature Converter (Easy)
def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32


output_temperature1 = celsius_to_fahrenheit(0)
output_temperature2 = celsius_to_fahrenheit(25)
output_temperature3 = celsius_to_fahrenheit(100)

# ? print(output_temperature1)
# ? print(output_temperature2)
# ? print(output_temperature3)

# * Question 2: Even or Odd Checker (Medium)


def check_even_odd(num):
    """takes a num and tell whether even or odd"""
    isDivisible = num % 2

    if isDivisible:
        return "odd"

    return "even"


num1 = check_even_odd(2)
num2 = check_even_odd(0)
num3 = check_even_odd(7)

# ? print(num1)
# ? print(num2)
# ? print(num3)


# * Question 3: Shopping Cart Total (Challenging)
def calculate_total(item1_price, item2_price, item3_price):
    """calculate total bill and adds 10% tax
    Return multiple value
    unpack tuple
    """
    subtotal = item1_price + item2_price + item3_price
    tax = subtotal * 0.10  # 10% tax
    total = subtotal + tax
    return subtotal, tax, total


# subtotal, tax, total = calculate_total(50, 30, 20)
# print(subtotal, tax, total)


"""
Q13.
Write a function that:
Takes a list of numbers
Returns the largest number in the list
"""

def largest_num(nums):
    biggest_num = nums[0]
    for num in nums:
        if num > biggest_num:
            biggest_num = num
    return biggest_num


# dummy_list = [0, 4, 3, 5, 6, 2, 4, 8]
# print(largest_num(dummy_list))


