# How to create Class in Python 

# class House:
#     floor = 3
#     door = 5 
#     room = 2 

# house = House()

# print(house.floor)
# print(house.door)
# print(house.room)

class Animal:
    color = ""
    year = 0

dog = Animal()

dog.color = "Black"
dog.year = 3

cat = Animal()

cat.color = "White"
cat.year = 1

# print("=====This is animal information====")
# print(f"Dog's color is {dog.color}")
# print(f"Dog's year old is {dog.year}")
# print(f"Cat's color is {cat.color}")
# print(f"Cat's year old is {cat.year}")

# Method in Class

class Person:
    name = "Sokha"
    age = 21
    gender = "Male"
    school = "Jomnum-Tech"
    graduated = False

    def show_info(self):
        print(f"My name is {self.name}")
        print(f"My age is {self.age}")
        print(f"My gender is {self.gender}")
        print(f"My school is {self.school}")
        print(f"Graduated : {self.graduated}")

# sokha = Person()
# sokha.show_info()

# Constructor in Class

class Job:
    def __init__(self, title, type, salary):
        self.title = title
        self.type = type
        self.salary = salary

    def show_info(self):
        print(f"Job title : {self.title}")
        print(f"Job type : {self.type}")
        print(f"Job Salary : {self.salary}")

it = Job("IT", "Full Time", 1000)
accounting = Job("Accounting", "Full Time", 800)

it.show_info()
accounting.show_info()

