try:
    with open("file.txt") as file:
        print(file.read())
except FileNotFoundError:
    print("File not found.")

new_list = [0, 1]
try:
    print(new_list[0])
    print(new_list[5])
except IndexError:
    print("Index Error")


try:
    num = int(input("Enter a number: "))
except ValueError:
    print("Invalid input")
else:
    print(type(num))