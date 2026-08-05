# x = input("Enter Number 1: ")
# y = input("Enter Number 2: ")
#
# try:
#     z = x/ int(y)
# except ZeroDivisionError:
#     print("Division by Zero Exception")
#     z = None
# except TypeError as e:
#     # print("Which Type of Exception? ", type(e).__name__)
#     print("You forgot to convert str to int")
#     z = None
#
# print("Division is: ",z)

## Exercise: Python Exception Handling

# 1. Write a Python program that takes a numeric grade from the user (between 0 and 100), and prints the corresponding letter grade:
#
# ```
# 90–100 → A
# 80–89  → B
# 70–79  → C
# 60–69  → D
# <60    → F
# ```
#
# 2. Your program should handle the following exceptions:
#    - If the user enters a non-numeric value, catch the `ValueError` and display a user-friendly message.
#    - If the user enters a number outside the valid range (0 to 100), raise a `ValueError` yourself with a custom message.
#
# 3. Use the `try–except–else–finally` structure:
#    - `try`: Attempt to parse the input and compute the letter grade.
#    - `except`: Handle conversion errors and invalid ranges.
#    - `else`: Print the final grade if everything was successful.
#    - `finally`: Print a goodbye message like `"Thank you for using the Grade Calculator. Goodbye!"` no matter what.
#
# [Solution](https://github.com/codebasics/py/blob/master/Basics/Exercise/15_exception_handling/exception_handling_solution.py)

# Kalp Doshi's Solution

try:
    grade = int(input("Please Enter number: "))

    if grade < 0 or grade > 100:
        raise ValueError("You entered an outside range number")

except ValueError as e:
    print(e)

else:
    if grade >= 90:
        print("You got 'A' Grade!")
    elif grade >= 80:
        print("You got 'B' Grade!")
    elif grade >= 70:
        print("You got 'C' Grade!")
    elif grade >= 60:
        print("You got 'D' Grade!")
    else:
        print("You are Fail, You got F Grade!")

finally:
    print("Thank you for using the Grade Calculator. Goodbye!")
