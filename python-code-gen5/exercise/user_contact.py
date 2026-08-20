"""
    User Contact Program
    Objective
    1/. Save Contact in the File
    2/. View All Contact in the File
    3/. Delete Contact
    4/. Exit 
"""

def create_contact():
    username = input("Enter Username: ")
    phone = input("Enter Phone Number: ")

    with open("contacts.txt", "a") as file:
        file.write(f"{username}, {phone}\n")

    print("New contact created successfully!!!")

def view_contact():
    with open("contacts.txt", "r") as file:
        if not file:
            print("No contact saved")

        for line in file:
            username, phone = line.strip().split(",")
            print(f"Username: {username}, Phone: {phone}")

def main():
    while True:
        print("1/. View Contacts")
        print("2/. Save Contact")
        print("3/. Exit")

        choice = input("Enter Choice (1-3): ")
        match choice:
            case "1":
                view_contact()
            case "2":
                create_contact()
            case "3":
                print("Exiting Program...")
                break
            case _:
                print("INVALID")

if __name__ == "__main__":
    main()
