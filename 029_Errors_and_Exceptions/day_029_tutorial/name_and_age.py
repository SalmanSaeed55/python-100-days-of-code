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
    else:
        if age < 0:
            print("Age cannot be negative")
        else:
            break
    finally:
        print("Age cannot be negative")