# Encapsulation in Python

# class Person:
#     def __init__(self, id, name, dob):
#         # public
#         self.id = id
#         # protected
#         self._dob = dob
#         # private
#         self.__name = name
#         self.__wallet = 500
        
# p1 = Person(101, "Bopha", "01/01/2000")

# Name Mangling
# print(p1._Person__wallet)

# class Bank:
#     def __init__(self, balance, id):
#         self.__balance = balance
#         self.__id = id

#     # getter
#     @property
#     def balance(self):
#         return self.__balance

#     @property
#     def id(self):
#         return self.__id

#     # setter
#     @balance.setter
#     def balance(self, value):
#         self.__balance = value

# bank1 = Bank(5000, "1a")

# bank1.balance = 1000
# print(bank1.balance)


class Product:
    def __init__(self, name, price, qty):
        self.__name = name
        self.__price = price
        self.__qty = qty

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        self.__price = value

    @property
    def qty(self):
        return self.__qty

    @qty.setter
    def qty(self, value):
        self.__qty = value
    
    def show_product(self):
        print(f"Product name is {self.name}")
        print(f"Price is {self.price}")
        print(f"Quantity is {self.qty}")

    def change_product(self, price):
        self.price = price

phone = Product("Iphone18", 2500, 10)
phone.change_product(2700)
phone.show_product()

