# Polyphorphism

# class Animal:
#     def make_sound(self):
#         print("making sound")

# class Cat(Animal):
#     def make_sound(self):
#         print("meow meow!!!")

# class Dog(Animal):
#     def make_sound(self):
#         print("woof woof!!!")

# cat = Cat()
# cat.make_sound()
# dog = Dog()
# dog.make_sound()

# class Animal():
#     def make_sound(self, sound):
#         print(f"making sound {sound}")

# cat = Animal()
# cat.make_sound("Meow")    
# dog = Animal()
# dog.make_sound("Woof")    

# class ATM:
#     def __init__(self):
#         pass

#     def widthdraw(self):
#         print("Withdrawing Money")

# class Card(ATM):
#     def widthdraw(self):
#         print("Withdrawing Money from Card")

# class QRScan(ATM):
#     def widthdraw(self):
#         print("Widthdrawing Money from QR Code")

# card = Card()
# card.widthdraw()

# qr = QRScan()
# qr.widthdraw()

class Internet:
    def __init__(self, name, speed, price):
        self.name = name
        self.speed = speed
        self.price = price 

    def show_name(self):
        print(f"Internet's Provider : {self.name}")

class Smart(Internet):
    def show_name(self):
        print(f"====Smart - Internet Service Provider (ISP)====")
        print(f"Internet's Provider : {self.name}")
        print(f"Internet's Speed : {self.speed}")
        print(f"Internet's Price : {self.price}")

class Cellcard(Internet):
    def show_name(self):
        print(f"====Cellcard - Internet Service Provider (ISP)====")
        print(f"Internet's Provider : {self.name}")
        print(f"Internet's Speed : {self.speed}")
        print(f"Internet's Price : {self.price}")

class Metfone(Internet):
    def show_name(self):
        print(f"====Metfone - Internet Service Provider (ISP)====")
        print(f"Internet's Provider : {self.name}")
        print(f"Internet's Speed : {self.speed}")
        print(f"Internet's Price : {self.price}")

smart = Smart("Smart Axiata", "2GB", "16$")
cellcard = Cellcard("Cellcard", "1GB", "8$")
metfone = Metfone("Metfone", "500MB", "5$")

ISP = [smart, cellcard, metfone]

for isp in ISP:
    isp.show_name()