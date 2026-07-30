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


def sum(a, b=0):
    """
    :param a:
    :param b:
    :return:
    """
    print(f"A : {a}")
    print(f"B : {b}")
    total = a + b
    print(f"Total inside function : {total}")
    return total

number = sum(5,6)
number_2 = sum(b=5, a=6)
number_3 = sum(5)

print(f"Total outside function : {number}")
print(f"Total  outside function : {number_2}")
print(f"Total outside function : {number_3}")