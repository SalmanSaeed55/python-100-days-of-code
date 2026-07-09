# Default Values
def my_function(a=1, b=2, c=3):
    print(a, b, c)

my_function()
my_function(a=10)
my_function(a=20, b=30)
my_function(a=20, b=30, c=10)

print()

# Unlimited Arguments
def add(*args):
    total = 0
    for num in args:
        total += num
    print(total)

add(1, 2, 3, 4) # All passed through as a tuple
print()

# Key word arguments
def calculate(**kwargs):
    for key, value in kwargs.items():
        print(key, value)

calculate(add=3, multiply=5, divide=2) # All passed through as a dictionary

