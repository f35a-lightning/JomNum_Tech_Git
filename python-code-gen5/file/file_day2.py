# using with statement 

FILE_NAME = "new_text.txt"

CREATE_MODE = "a"
READ_MODE = "r"

with open(FILE_NAME, CREATE_MODE) as file:
    file.write(f"New text file created!!\n")

with open(FILE_NAME, "r") as file:
    files = file.readlines()
    print(files)



