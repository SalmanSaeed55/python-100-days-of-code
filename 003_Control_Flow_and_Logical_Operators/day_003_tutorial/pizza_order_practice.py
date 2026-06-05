print("Welcome to the Pizza Order deliveries")

total = 0
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni? Y or N: ")
extra_cheese = input("Do you want cheese? Y or N: ")

if size == "S":
    total += 15
    if pepperoni == "Y":
        total += 2
elif size == "M":
    total += 20
    if pepperoni == "Y":
        total += 3
elif size == "L":
    total += 25
    if pepperoni == "Y":
        total += 3
else:
    print("Please enter a valid size")

if extra_cheese == "Y":
    total += 1

print(f"Your final total is: £{total}")