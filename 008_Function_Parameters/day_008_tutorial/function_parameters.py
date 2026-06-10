def greet():  # Is quite static in terms of greeting different people
    print("Hello")
    print("How are you?")
    print("I hope you're doing fine")


greet()


def new_greeting(name):  # Parameters allow arguments to be passed into a function from the main program
    print(f"Hello, {name}!")
    print("How are you?")
    print("I hope you're doing fine")


new_greeting(input("What is your name? "))
