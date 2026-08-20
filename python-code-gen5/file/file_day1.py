# Python File I/O

# File Operation

# Opening File

# r - read mode
# w - write mode
# a - append mode
# x - create mode
try:
    file = open("another_file.txt", "x")
    file.write("By Jomnum-Tech 2026")
    # Closing File
    file.close()
except FileExistsError:
    print("File already exist")


