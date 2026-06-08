def my_function():  # Defins the function explicitly
    print("Hello")
    print("Bye")


my_function()  # Calls the function


def my_function2():
    name = input("Enter your name: ")
    return name


name_inp =my_function2()
print(name_inp)