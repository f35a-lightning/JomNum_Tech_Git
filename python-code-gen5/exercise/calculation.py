# Objective : Learn create function and use it

# Show information
# Operate
# Show result

# option = ""

def show_info():
    
    print("------------Calculation---------------")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

def operate():
    option = input("Enter option (1-5): ")
    match option:
        case "1":
            num1 = int(input("Enter first number: "))
            num2 = int(input("Enter second number: "))
            total = num1 + num2
            show_result()
            print(f"Total Number is : {total}")
        case "2":
            num1 = int(input("Enter first number: "))
            num2 = int(input("Enter second number: "))
            total = num1 - num2
            show_result()
            print(f"Total Number is : {total}")
        case "3":
            pass
        case "4":
            pass
        case "5":
            pass
        case _:
            pass

def show_result():
    print("-" * 10 + "Result" + "-" * 10)
    

while True:
    show_info()
    operate()