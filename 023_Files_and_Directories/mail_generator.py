name_list = []

with open("names.txt") as names:
    for name in names:
        name_list.append(name.strip())

with open("letter_template.txt", "r") as template:
    template = template.read()

with open("letter_template.txt", "a+") as names:
    for name in name_list:
        letter = template.replace("[name]", name)
        with open(f"./generated_letters/letter_for_{name.lower()}.txt", "w") as letter_file:
            letter_file.write(letter)

print("Done")