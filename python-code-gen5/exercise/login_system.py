"""
This is login system built with Python Dictionary
"""

"""
Flow

- User input username or password
- System check and verify
- Output login success or failed
"""

profile = {
    "username": "admin",
    "password": "123456"
}

def login():
    attempts = 3
    while attempts >= 0:
        if attempts == 0:
            print("You have banned")
            break
        
        username = input("Enter Username: ")
        password = input("Enter password: ")

        if profile["username"] == username and profile["password"] == password:
            print("Login Successfully")
        else:
            print("Login Failed")
            attempts -= 1

login()