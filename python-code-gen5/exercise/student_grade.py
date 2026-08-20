# This is student grade calucation system 
"""
Find total score, average score, and grade
"""

print("-" * 50)
print("Welcome to Student Grade Calculator")
print("-" * 50)

# Math, IT, English

student_name = input("Enter Student name: ")
math_score = int(input("Enter Math Score: "))
it_score = int(input("Enter IT Score: "))
english_score = int(input("Enter English Score: "))

# total Score
total_score = math_score + it_score + english_score

# average score 
average_score = total_score / 3

# output
print("-----------------------------------")

print(f"Student name: {student_name}")
print(f"Total Score: {total_score}")
print(f"Average Score: {average_score}")

# grade - condition
if average_score >= 90:
    print("This student get grade A")
elif average_score >= 80:
    print("This student get grade B")
elif average_score >= 70:
    print("This student get grade C")
elif average_score >= 60:
    print("This student get grade D")
elif average_score >= 50:
    print("This student get grade E")
elif average_score < 50:
    print("This student get grade F")
else:
    print("INVALID")







