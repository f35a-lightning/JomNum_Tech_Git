# This is food menu
# Using Match with While loop

while True:
    customer = input("Enter Customer name: ")
    food = input("Enter food: ")

    match food:
        case "pizza":
            print("-------Pizza Menu-------")
            print("Price : 11.99")
        case "burger":
            print("This is burger")
        case "drink" | "coca" | "pepsi":
            print("This is drink")
        case _:
            print("Item is not available")