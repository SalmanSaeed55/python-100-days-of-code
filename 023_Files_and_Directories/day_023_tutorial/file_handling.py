file = open("my_file.txt")
contents = file.read()
print(contents)

file.close()

# More preferred method
with open("my_file.txt", "r") as file:
    contents = file.read()

print(contents)

# Writing to a file
with open("my_file.txt", "w") as file:
    file.write("New text")