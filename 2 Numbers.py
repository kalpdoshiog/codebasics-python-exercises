# print(12 + 3)
#
# print(4 - 3)
#
# print(5 / 2)
#
# print(5 * 5)
#
# print(11 % 2)
#
# print(3 ** 2)
#
#
# nyc_bal = 188
# bal_pits = 356
#
# total_distance = nyc_bal + bal_pits
# print(total_distance)
#
#
# mph = 65
# total_time = total_distance / mph
#
# print(total_time)
#
# print(round(total_time, 2))
#
# print(round(total_time, 3))
#
#
# # Integer = 2 , 4 ,6 ,7 ,8 , -6 , -4 , -56546 It is Integer because it does not have Fractional part. It is also called a whole number basically
# # Float = 2.45 , 5.78899 , -1345.576767 It is a float number because it has a Fractional part
#
# print(10+2*3) # PEMDAS - Parentheses, Exponents, Multiplication and Division, Addition and Subtraction.
#
# print((10+2)*3)
#
# print(6 - 5.7)
#
# print(round(6 - 5.7, 2))



# Exercise: Numbers in python
# 1. You have a football field that is 92 meter long and 48.8 meter wide. Find out total
# area using python and print it.

# 2. You bought 9 packets of potato chips from a store. Each packet costs 1.49 dollar
# and you gave shopkeeper 20 dollar. Find out using python, how many dollars is the shopkeeper going to give you back?

# 3. You want to replace tiles in your bathroom which is exactly square and 5.5 feet
# is its length. If tiles cost 500 rs per square feet, how much will be the total
# cost to replace all tiles. Calculate and print the cost using python
# (Hint: Use power operator ** to find area of a square)

# 4. Print binary representation of number 17
#
# [Solution](https://github.com/codebasics/py/blob/master/Basics/Exercise/3_numbers/3_numbers_exercise.py)


# 1. Solution
football_field_Length = 92
football_field_width = 48.8

total_area = football_field_Length * football_field_width
print(total_area)
print(round(total_area, 2))

# 2. Solution
potato_pack = 1.49

total_cost = 1.49 * 9

total_money_gave = 20

total_money_return = total_money_gave - total_cost

print(total_money_return)

# 3. Solution

area_of_tiles = 5.5 ** 2

total_cost_of_tiles = area_of_tiles * 500
print(total_cost_of_tiles)

# 4. Solution

number = 17

binary_num = f"{number:b}" #Used google for this as video does not taught this.

print(binary_num)
