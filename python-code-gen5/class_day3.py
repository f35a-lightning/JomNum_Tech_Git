# Inheritance in Python

# Single Inheritance 

class Teacher:
    def __init__(self, name, classroom, gender):
        self.__name = name
        self.__classroom = classroom
        self.__gender = gender
        print("Teacher has created")

class Student(Teacher):
    pass

# Kanika = Student("Kanika", "Grade A", "Female")

# Multiline Inheritance

# class A:
#     def show_a(self):
#         print("This is Class A")

# class B(A):
#     def show_b(self):
#         print("This is Class B")

# class C(B):
#     pass

# # A -> B -> C

# c = C()
# c.show_b()

# Multilevel Inheritance

# class A:
#     def show(self):
#         print("This is CLASS A")

# class B(A):
#     pass

# class C(A):
#     pass

# class D(A):
#     pass

# # A -> B
# # A -> C
# # A -> D

# obj = D()
# obj.show()

class Bank:
    def __init__(self, balance):
        self.__balance = balance

    @property
    def balance(self):
        return self.__balance

    # To Check Total Balance
    def check_balance(self):
        print(f"Total Balance: {self.balance}")

class Person(Bank):
    def __init__(self, balance, name):
        super().__init__(balance)
        self.__name = name

    @property
    def name(self):
        return self.__name

    # To Check User Profile
    def check_profile(self):
        print(f"Account Name: {self.name}")

p1 = Person(2000, "Julie")
p1.check_profile()
p1.check_balance()

# Hybrid Inheritance 

class A:
    def show(self):
        print("CLASS A")

class B:
    def show(self):
        print("CLASS B")

class C(B, A):
    pass

class D(C):
    pass

# obj = C()
# obj.show()
    

    