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

