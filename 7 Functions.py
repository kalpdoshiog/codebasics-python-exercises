# Without using function

tom_expense_list = [580, 305, 240, 710]
joe_expense_list = [320, 670, 180, 760]

total = 0

for item in tom_expense_list:
    total += item
print(total)

total = 0

for item in joe_expense_list:
    total += item
print(total)

# Here we are repeating same code again and again, what if we need to do this for 100 lists?
# So we will use functions.