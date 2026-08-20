# Abstraction in Python

from abc import ABC, abstractmethod

# class Person(ABC):
#     @abstractmethod
#     def show_name(self):
#         pass

#     @abstractmethod
#     def show_age(self):
#         pass

#     @abstractmethod
#     def show_gender(self):
#         pass

# class Student(Person):
#     def show_name(self):
#         print("This is student name")
#     def show_age(self):
#         print("This is student age")
#     def show_gender(self):
#         print("This is student gender")

# st1 = Student()
# st1.show_name()
# st1.show_age()
# st1.show_gender()

class School(ABC):
    def __init__(self, name, year):
        self.__name = name
        self.__year = year

    @property 
    def name(self):
        return self.__name
    @abstractmethod
    def show_name(self):
        pass

    def show_year(self):
        print("School is operating for 5 years")

class Teacher(School):
    def __init__(self, name, year, position):
        super().__init__(name, year)
        self.__position = position
    
    def show_name(self):
        print(f"Teacher name is {self.name}")

class Student(School):
    def show_name(self):
        print("This is student name")

t1 = Teacher("Vibol", 3, "History")
t1.show_name()
s1 = Student("Kaka", 5)
s1.show_name()