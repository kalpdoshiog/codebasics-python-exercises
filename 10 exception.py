x = input("Enter Number 1: ")
y = input("Enter Number 2: ")

try:
    z = x/ int(y)
except ZeroDivisionError:
    print("Division by Zero Exception")
    z = None
except TypeError as e:
    # print("Which Type of Exception? ", type(e).__name__)
    print("You forgot to convert str to int")
    z = None

print("Division is: ",z)

