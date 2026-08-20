# Dictionary in Python

# Create dictionary

person = {
    "name": "Vichet",
    "age": 18,
    "married": False,
    "grade": "A"
}

# Modify Key in dictionary
person["class"] = "Class A"
person["age"] = 19
person["married"] = True
person["grade"] = "C"

# Output
# print(f"His class is {person["class"]}")
# print(person)

school = {
    "name": "Jomnum-Tech",
    "location": "Phnom Penh",
    "class": ["Python", "Web Design", "SQL", "FastAPI", "Java"]

}

# nested dictionary

classroom = {
    "id": 101,
    "info": {
        "class_name": "Python",
        "instructor": "Jomnum-Tech"
    }
}

# print(classroom["info"]["instructor"])
# print(school["class"][len(school["class"])-1])

# Loop in dictionary

profile = {
    "first_name": "kaka",
    "last_name": "jeje",
    "active": True
}

# membership
if "middle_name" in profile:
    print("Key is Exist")
else:
    print("Key is not exist")

# iterate only key
for key in profile.keys():
    print(f"{key}")

# iterate only value
for value in profile.values():
    print(f"{value}")

# iterate both key and value
for key, value in profile.items():
    print(f"{value}")

# constructor

country = dict(name="Cambodia", capital="Phnom Penh", location="Southest-Asia")

print(country)