


while True:
    try:
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        operation = input("Enter operation: [+, -, *, /]: ")
        if operation not in ["+", "-", "*", "/"]:
            raise ValueError("Invalid operation. Please enter one of +, -, *, /.")
    except ValueError as e:
        print(e)
    else:
        break