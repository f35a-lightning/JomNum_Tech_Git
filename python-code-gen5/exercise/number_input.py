"""
This is simple program that user can input number 
"""

print("--------Welcome to Number Input System--------")

# User must input number

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

total = num1 + num2

# Output result

print(type(total))

print(f"Total Number is: {total}")