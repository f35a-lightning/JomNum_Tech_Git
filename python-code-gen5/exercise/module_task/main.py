from operation import sum, sub, mul, div
from display import show_result

list_operation = [sum, sub, mul, div]

# data = {
#     10: 20,
#     80: 5,
#     25: 4,
#     200: 25
# }

# for operation in list_operation:
#     for key, value in data.items():
#         print(show_result(operation(key, value)))

print(show_result(sum(5,7)))
print(show_result(sub(200,50)))
print(show_result(mul(4,5)))
print(show_result(div(180,60)))
