# Without using function

# tom_expense_list = [580, 305, 240, 710]
# joe_expense_list = [320, 670, 180, 760]
#
# total = 0
#
# for item in tom_expense_list:
#     total += item
# print(total)
#
# total = 0
#
# for item in joe_expense_list:
#     total += item
# print(total)

# Here we are repeating same code again and again, what if we need to do this for 100 lists?
# So we will use functions.

# Using Functions

# tom_expense_list = [580, 305, 240, 710]
# joe_expense_list = [320, 670, 180, 760]
#
# def total_expense(exp):
#     total = 0
#     for item in exp:
#         total += item
#     return total
#
# tom_expense = total_expense(tom_expense_list)
# joe_expense = total_expense(joe_expense_list)
#
# print(f"Tom's total expense is : {tom_expense}")
# print(f"Joe's total expense is : {joe_expense}")


# def sum(a, b=0):
#     """
#     :param a:
#     :param b:
#     :return:
#     """
#     print(f"A : {a}")
#     print(f"B : {b}")
#     total = a + b
#     print(f"Total inside function : {total}")
#     return total
#
# number = sum(5,6)
# number_2 = sum(b=5, a=6)
# number_3 = sum(5)
#
# print(f"Total outside function : {number}")
# print(f"Total  outside function : {number_2}")
# print(f"Total outside function : {number_3}")


# Exercise: Functions in python
# 1. Write a function called calculate_area that takes base and height as an input and returns and area of a triangle. Equation of an area of a triangle is,
# ```
# area = (1/2)*base*height
# ```
#
# 2. Modify above function to take third parameter shape type. It can be either "triangle" or "rectangle". Based on shape type it will calculate area. Equation of rectangle's area is,
# ```
# rectangle area=length*width
# ```
# If no shape is supplied then it should take triangle as a default shape
#
# 3. Write a function called print_pattern that takes integer number as an argument and prints following pattern if input number is 3,
# ```
# *
# **
# ***
# ```
# if input is 4 then it should print
# ```
# *
# **
# ***
# ****
# ```
# Basically number of lines it prints is equal to that number. (Hint: you need to use two for loops)
#
# [Solution](https://github.com/codebasics/py/blob/master/Basics/Exercise/10_functions/10_functions_exercise.py)

# Kalp Doshi's Solution

def calulate_area(base, height):
    area = (1/2) * base * height
    return area

area_of_a_triangle = calulate_area(5, 10)
print(area_of_a_triangle)