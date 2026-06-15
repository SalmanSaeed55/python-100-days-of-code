try:
    age = int(input("Enter your age: "))
except ValueError:
    print("Please enter an integer")
    age = int(input("Enter your age: "))

if age >= 18:
    print("You are eligible to drive.")
else:
    print("You are not eligible to drive.")