# Modulo `%` is used to get the remainder of a division

# Mini Challenge: Ask for a number and determine whether it is even or odd
number = int(input("Enter a number: "))

if number % 2 == 0: # An even number has no remainder
    print("Even")
else: # Else, it is an odd number
    print("Odd")