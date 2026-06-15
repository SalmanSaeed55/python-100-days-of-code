def my_function():  # Doesn't print anything because the condition is never met
    for i in range(1, 20):  # Upper bound is not included
        if i == 20:
            print(i)


my_function()


# Debugged code
def my_function():
    for i in range(1, 21):
        if i == 20:
            print(i)


my_function()