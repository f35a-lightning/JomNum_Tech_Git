# Match Statement 

day = "Thursday"

match day:
    case "Monday":
        print("Today is working day")
    case "Tuesday":
        print("Today is workding day")
    case "Wednesday" | "Thursday" | "Friday":
        print("Today is working day")
    case "Saturday" | "Sunday" :
        print("Today is relax day")
    case _: 
        print("INVALID")

# For Loop Statement
# Iterate from 1 - 10

# for i in range(1,11):
#     print(i)

# for i in range(0,5):
#     print(f"{i + 1}. Hello Python")

# for i in range(10,0,-2):
#     print(i)

# While Loop

# Infinite Loop
# i = 5
# while i > 0:
#     print(f"{i}. Yes i is bigger than zero")
#     i -= 1

# increment/decrement

# for i in range(1,11):
#     if i % 2 != 0:
#         continue
#     print(i)

for i in range(1,11):
    if i == 5:
        break
    print(i)



    