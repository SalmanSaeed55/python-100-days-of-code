# Basic if statements
print("Welcome to the roller coaster")
height = int(input("Please enter your height in centimeters: "))

if height > 120:  # checks if height is greater than 120cm
    print("You can ride the roller coaster")
else:  # if not height is less than or equal to 120cm
    print("You cannot ride the roller coaster")

print("-" * 20)
bill = 0

# Nested if statements
if height > 120:
    print("You can ride the roller coaster")
    age = int(input("Please enter your age: "))
    if age < 12:
        print("Child tickets are £5.00")
        bill += 5
    elif 12 <= age < 18:
        print("Teenage tickets are £7.00")
        bill += 7
    else:
        print("Adult tickets are £12.00")
        bill += 12

    wants_photo = input("Do you want a photo taken? 'y' or 'n': ")
    if wants_photo == "y":
        bill += 3

    print(f"Your final bill is: £{bill}")
else:
    print("You cannot ride the roller coaster")