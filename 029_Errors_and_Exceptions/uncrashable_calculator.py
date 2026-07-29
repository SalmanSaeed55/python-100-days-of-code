def number_inps():
    while True:
        try:
            num1 = int(input("Enter first number: "))
            num2 = int(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter numeric input.")
        else:
            return num1, num2

def operation_inps():
    while True:
        try:
            operation = input("Enter operation: [+, -, *, /]: ")
            if operation not in ["+", "-", "*", "/"]:
                raise ValueError("Invalid operation. Please enter one of +, -, *, /.")
        except ValueError as e:
            print(e)
        else:
            return operation

def main():
    num1, num2 = number_inps()
    operation = operation_inps()
    if operation == "+":
        print(f"{num1} + {num2} = {num1 + num2}")
    elif operation == "-":
        print(f"{num1} - {num2} = {num1 - num2}")
    elif operation == "*":
        print(f"{num1} * {num2} = {num1 * num2}")
    elif operation == "/":
        print(f"{num1} / {num2} = {num1 / num2}")

while True:
    main()
    choice = input("Do you want to perform another calculation? (y/n): ")
    if choice.lower() != "y":
        break