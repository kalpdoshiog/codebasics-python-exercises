# dic = {"tom" : 123456789,
#        "john": 123567890,
#        "bon" : 1234567890,
#        }
# print(dic)
#
# print(dic["tom"])
#
# dic["sam"] = 9876544521
#
# print(dic)
#
# del dic["sam"]
#
# print(dic)
#
# for key in dic:
#     print(f"Key : {key}, Value : {dic[key]}")
#
# for key, value in dic.items():
#     print(key,value)
#
# print("tom" in dic)
# print("samir" in dic)
#
# dic.clear()
# print(dic)
#
# tuple_point = (5,6)
#
# print(tuple_point)
# print(tuple_point[0])
# print(tuple_point[1])
from sys import set_coroutine_origin_tracking_depth

# tuple_point[0] = 1 We can not change values in tuples.

exercise = """
## Exercise: Python Dict and Tuples

### 1. Country Population Dictionary

We have the following information on countries and their population (in crores):

| Country | Population |
|---------|-----------:|
| China | 143 |
| India | 136 |
| USA | 32 |
| Pakistan | 21 |

Tasks:
1. Create a dictionary of countries and their populations.
2. Write a program that asks the user for one of these operations:
   - **print**
     ```
     china ==> 143
     india ==> 136
     usa ==> 32
     pakistan ==> 21
     ```
   - **add**
     - Ask for a country name.
     - If it already exists, print a message and do nothing.
     - Otherwise ask for its population, add it to the dictionary, and print the updated dictionary.
   - **remove**
     - Ask for a country name.
     - If it exists, remove it and print the updated dictionary.
     - Otherwise print "Country doesn't exist!"
   - **query**
     - Ask for a country name.
     - Print its population if it exists.

---

### 2. Stock Prices

| Stock | Prices |
|-------|----------------|
| info | [600, 630, 620] |
| ril | [1430, 1490, 1567] |
| mtl | [234, 180, 160] |

Tasks:
1. Ask the user for an operation:
   - **print**
     ```
     info ==> [600, 630, 620] ==> avg: 616.67
     ril ==> [1430, 1490, 1567] ==> avg: 1495.67
     mtl ==> [234, 180, 160] ==> avg: 191.33
     ```
   - **add**
     - Ask for stock ticker and price.
     - If the ticker exists, append the new price.
     - Otherwise create a new stock entry.

---

### 3. Circle Calculator

Write a function `circle_calc()` that:
- Takes radius as input.
- Returns:
  - Area
  - Circumference
  - Diameter

Call the function in the main program and print the returned values.
"""

# country_population = {"China":143,
#                       "India": 134,
#                       "Usa": 32,
#                       "Pakistan": 21}
#
# enter_operation = input("Please enter add, remove, or query : ").lower()
#
#
# if enter_operation == "add":
#     ask_country_name = input("Please enter country name : ").capitalize()
#     if ask_country_name in country_population:
#         print(f"This country ({ask_country_name}) data  already exits : {country_population[ask_country_name]}")
#     else:
#         aks_for_population = int(input("Please enter Population details : "))
#         country_population[ask_country_name] = aks_for_population
#         print(country_population)
#
# elif enter_operation == "remove":
#     ask_country_name = input("Please enter country name : ").capitalize()
#     if ask_country_name in country_population:
#         del country_population[ask_country_name]
#         print(country_population)
#     else:
#         print("Country does not exist")
# elif enter_operation == "query":
#     ask_country_name = input("Please enter country name : ").capitalize()
#     print(f"{ask_country_name} : {country_population[ask_country_name]}")

# stock_prices = {"info" : [600, 630, 620], "ril" : [1430, 1490, 1567], "mtl" : [234, 180, 160]}
#
# enter_operation_2 = input("Please enter which operation to perform: 'print' or 'add'? ").lower()
#
# if enter_operation_2 == "print":
#     for key in stock_prices:
#         print(f"{key} ==> {stock_prices[key]} ==> {round(sum(stock_prices[key])/len(stock_prices[key]),2)}")
#
#
# elif enter_operation_2 == "add":
#     enter_stock_ticker = input("Please enter Stock Ticker : ").lower()
#     enter_stock_ticker_price = int(input("Please enter Stock Ticker Price : "))
#     if enter_stock_ticker in stock_prices:
#         stock_prices[enter_stock_ticker].append(enter_stock_ticker_price)
#         print(stock_prices)
#
#     else:
#         stock_prices[enter_stock_ticker] = [enter_stock_ticker_price]
#         print(stock_prices)


def circle_calc(radius):
    diameter = radius * 2
    area = 3.14 * radius ** 2
    circumference = 2 * 3.14 * radius
    return area, diameter, circumference

input_radius = int(input("Please enter Radius : "))

area, diameter, circumference = circle_calc(input_radius)

print(area)
print(diameter)
print(circumference)

