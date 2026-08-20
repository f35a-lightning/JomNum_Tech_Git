# Exception in Python

# numbers = [2,4,6]

books = {
    "name": "Atomic Habit",
    "author": "James Clear",
}

try:
    print(books["name"])
except ZeroDivisionError:
    print("Cannot divide by zero")
except IndexError: 
    print("Index out of range")
except KeyError:
    print("Key in dictionary is not found")
finally:
    print("End of Exception")

print("Hello from Exception From Python")

print("--------------------------")

age = 16

if age < 18:
    raise ValueError("You are not eligible to join event")
else:
    print("You are eligible to join event")

# try:
#     num = int(input("Enter Number:"))
# except ValueError:
#     print("Invalid Value")

# try:
#     num = int(input("Enter Number: "))

# except ValueError:
#     print("Your input is not valid")
# finally:
#     print("End of exception")

# num = int(input("Enter number: "))

