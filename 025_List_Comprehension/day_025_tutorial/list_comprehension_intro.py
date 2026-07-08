numbers = [1, 2, 3]
new_numbers = [n + 1 for n in numbers]
print(new_numbers)

name = "Salman"
name_letters = [letter for letter in name]
print(name_letters)

# Conditional List Comprehension
name_letters_a = [letter for letter in name if letter == "a"]
print(name_letters_a)

names = ["Alice", "Bob", "Charlie", "David"]
short_names = [name for name in names if len(name) < 4]
print(short_names)