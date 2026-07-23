while True:
    name = input("Enter your name: ").strip()
    if name:
        break
    print("Name cannot be empty")

while True:
    try:
        age = int(input("Enter your age: "))
        break
    except ValueError:
        print("Please enter a valid whole number for age")

print(f"Hello {name}, you are {age} years old")