text = "Ice Cream"

print(text)

print(text[0]) # Index Zero, Python strings starts with zero (0).

print(text[1]) # It will print a char from index 1 of text variable.

print(text[0:3]) # 0 is included but 3 is not means n-1 (3-1) = 2 so it will go upto 2 only

print(text[4:]) # It will go till end

print(text[:9]) # It will start from zero and go till 8 as (9-1) = 8

# Strings can define by both "" and ''

text = "Let's go eat"

text = 'Let\'s go eat' # Both works

text = 'Hello "World!"' # This also works

address = '''2 Purple Street,
New York, 
USA'''  # THis is multi line string.

print(address)

s1 = " Hello "
s2 = "World "

print(s1 + s2) #Concatenation

# OR

s1 = "Hello"
s2 = "World"

print(s1 + " " + s2)


states_in_usa = "Total number of states in The USA # "
number = 51

print(states_in_usa + str(number))

## Exercise: String in Python

# 1. Create 3 variables to store street, city and country, now create address variable to
# store entire address. Use two ways of creating this variable, one using + operator and the other using f-string.
# Now Print the address in such a way that the street, city and country prints in a separate line

# 2. Create a variable to store the string "Earth revolves around the sun"
#     1. Print "revolves" using slice operator
#     2. Print "sun" using negative index

# 3. Create two variables to store how many fruits and vegetables you eat in a day.
# Now Print "I eat x veggies and y fruits daily" where x and y presents vegetables and fruits that you eat everyday. Use python f string for this.

# 4. I have a string variable called s='maine 200 banana khaye'. This of course is a
# wrong statement, the correct statement is 'maine 10 samosa khaye'.
# Replace incorrect words in original strong with new ones and print the new string.
# Also try to do this in one line.
#
# [Solution](https://github.com/codebasics/py/blob/master/Basics/Exercise/4_strings/4_string_exercise_answer.py)

street = "67 Purple Street \n"
city = "Six Seven \n"
country = "Canada \n"

address = street + city +  country
address_2 = f"{street}{city}{country}"

print(address)
print(address_2)

