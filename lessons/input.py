"""Demonstrates asking the user for input."""


user_name: str = input("What is your name? ")
print("Hello, " + user_name + ", good morning!")
print("You are awesome, " + user_name)

choice: int = int(input("Enter a number"))

# Implement this logic
# A < 25 
# B >= 25 and <50 
# C > 75
# D >=50 and <=75

if choice < 25:
    print("A")
else:
    if choice < 50:
        print("B")
        if choice > 75: 
            print("C")
        else: 
            print("D")
