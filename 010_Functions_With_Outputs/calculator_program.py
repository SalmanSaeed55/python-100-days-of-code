def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


print("Welcome to the Calculator Program!")

calc_operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}
usage = True
num1 = None

while usage:
    if num1 is None:
        num1 = int(input("Enter the first number: "))

    operator = ""
    while operator not in calc_operations:
        operator = input("Please enter one of the following options: +, -, *, /: ")

    num2 = int(input("Enter the second number: "))

    solution = calc_operations[operator](num1, num2)
    print(f"{num1} {operator} {num2} = {solution}")

    exit_calc = input("Do you want to exit the calculator? (y/n): ")
    if exit_calc == "y":
        print("Closing the calculator...")
        usage = False
    else:
        reuse_num1 = input(f"Do you want to reuse {solution} for the next calculation? (y/n): ")
        if reuse_num1 == "y":
            num1 = solution
        else:
            num1 = None