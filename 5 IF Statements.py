number = int(input("Enter a Number: "))

if number % 2 == 0 :
    print("Number is Even")
else:
    print("Number is Odd")


indian = ["samosa",
          "daal",
          "naan",
          ]

chinese = ["egg roll",
           "pot sticker",
           "fried rice",
           ]

italian = ["pizza",
           "pasta",
           "risotto",]

dish_name = input("Enter your favorite dish name: ")

if dish_name in indian:
    print("Indian Cuisine")
elif dish_name in chinese:
    print("Chinese Cuisine")
elif dish_name in italian:
    print("Italian Cuisine")
else:
    print("You are eating different cuisine!")

## Exercise: Python If Condition
# 1. Using following list of cities per country,
#     ```
#     india = ["mumbai", "banglore", "chennai", "delhi"]
#     pakistan = ["lahore","karachi","islamabad"]
#     bangladesh = ["dhaka", "khulna", "rangpur"]
#     ```
#     1. Write a program that asks user to enter a city name and it should tell which country the city belongs to
#     2. Write a program that asks user to enter two cities and it tells you if they both are in same country or not. For example if I enter mumbai and chennai, it will print "Both cities are in India" but if I enter mumbai and dhaka it should print "They don't belong to same country"


# 2. Write a python program that can tell you if your sugar is normal or not. Normal fasting level sugar range is 80 to 100.
#     1. Ask user to enter his fasting sugar level
#     2. If it is below 80 to 100 range then print that sugar is low
#     3. If it is above 100 then print that it is high otherwise print that it is normal
#
# [Solution - Exercise 1.i](https://github.com/codebasics/py/blob/master/Basics/Exercise/8_if/8_exercise1_1.py)
#
# [Solution - Exercise 1.ii](https://github.com/codebasics/py/blob/master/Basics/Exercise/8_if/8_exercise1_2.py)
#
# [Solution - Exercise 2](https://github.com/codebasics/py/blob/master/Basics/Exercise/8_if/8_exercise2.py)


india = ["Mumbai", "Bangalore", "Chennai", "Delhi"]
pakistan = ["Lahore","Karachi","Islamabad"]
bangladesh = ["Dhaka", "Khulna", "Rangpur"]

enter_your_city = input("Enter your city name: ")

if enter_your_city in india:
    print(f"Your city {enter_your_city } is in India")
elif enter_your_city in pakistan:
    print(f"Your city {enter_your_city} is in Pakistan")
elif enter_your_city in bangladesh:
    print(f"Your city {enter_your_city} is in Bangladesh")
else:
    print(f"Your city {enter_your_city} is not listed.")

enter_city_1 = input("Enter city 1 name: ")
enter_city_2 = input("Enter city 2 name: ")

if enter_city_1 in india and enter_city_2 in india:
    print(f"Both cities {enter_city_1} and {enter_city_2} are in India")
elif enter_city_1 in pakistan and enter_city_2 in pakistan:
    print(f"Both cities {enter_city_1} and {enter_city_2} are in Pakistan")
elif enter_city_1 in bangladesh and  enter_city_2 in bangladesh:
    print(f"Both cities {enter_city_1} and {enter_city_2} are in Bangladesh")
else:
    print(f"Both cities {enter_city_1} and {enter_city_2} are not in same country")


suger_level = int(input("Enter your fasting sugar level: "))

if suger_level <80:
    print("Your sugar level is low!")
elif 80 <= suger_level <=100:
    print("Your sugar level is normal")
else:
    print("Your sugar level is high")