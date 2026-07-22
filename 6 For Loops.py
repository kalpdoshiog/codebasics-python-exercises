# expense = [2350, 2100, 3450, 1679, 5321]
#
# total = 0
# for item in expense:
#     total += item
#
# print(total)


# for number in range(1, 11):
#     print(number)
#
# for number in range(1, 11):
#     print(number*number)
#
#
# expense = [2350, 2100, 3450, 1679, 5321]
# total = 0
# for item in range(len(expense)):
#     print(f"Month :", (item+1), "Expense :" , expense[item])
#     total += expense[item]
# print(f"Total expense is : {total}")

# key_location = "chair"
# locations = ["garage", "living room", "kitchen", "chair", "bedroom", "bath room"]
#
# for key in locations:
#     if key==key_location:
#         print(f"Key is found : {key}")
#         break
#     else:
#         print(f"Key is not found : {key}")

# for i in range(1,6):
#     if i%2==0:
#         continue
#     print(i*i)
# i = 1
# while i<=5:
#     print(i)
#     i += 1

## Exercise: Python for loop
# 1. After flipping a coin 10 times you got this result,
# ```
# result = ["heads","tails","tails","heads","tails","heads","heads","tails","tails","tails"]
# ```
# Using for loop figure out how many times you got heads
#
# 2. Print square of all numbers between 1 to 10 except even numbers
# 3. Your monthly expense list (from Jan to May) looks like this,
# ```
# expense_list = [2340, 2500, 2100, 3100, 2980]
# ```
# Write a program that asks you to enter an expense amount and program
# should tell you in which month that expense occurred. If expense is not
# found then it should print that as well.
#
# 4. Lets say you are running a 5 km race. Write a program that,
#    1. Upon completing each 1 km asks you "are you tired?"
#    2. If you reply "yes" then it should break and print "you didn't finish the race"
#    3. If you reply "no" then it should continue and ask "are you tired" on every km
#    4. If you finish all 5 km then it should print congratulations message
#
# 5. Write a program that prints following shape
# ```
# *
# **
# ***
# ****
# *****
# ```
#
#
# [Solution](https://github.com/codebasics/py/blob/master/Basics/Exercise/9_for/9_for_exercise.py)

# Kalp Doshi's Solution

# result = ["heads","tails","tails","heads","tails","heads","heads","tails","tails","tails"]
#
# num_of_heads = 0
# for heads in result:
#     if heads == "heads":
#         num_of_heads += 1
#
# print(num_of_heads)

# for i in range(1,11):
#     if i % 2==0:
#         continue
#     else:
#         print(i*i)
# found = False
# expense_list = [2340, 2500, 2100, 3100, 2980]
# month_list = ["January", "February", "March", "April", "May"]
#
# enter_amount = int(input("Please enter amount : "))
#
# for i in range(len(expense_list)):
#     if expense_list[i] == enter_amount:
#         print(f"The amount {enter_amount} was spent in {month_list[i]}")
#         found = True
#         break
# if not found:
#     print(f"The amount {enter_amount} was not spent in logged months.")

# km = 0
#
# for i in range(5):
#     km += 1
#     if km == 5:
#         print(f"Congratulation! You have completed {5} KM Race")
#         break
#     print(f"You have completed {km} KM")
#     ask = input("Are you tired? ").lower()
#     if ask == "yes":
#         print("You didn't finished the race")
#         break
#     elif ask == "no":
#         continue

stars = ""
for i in range(1,6):
    stars += "*"
    print(stars)