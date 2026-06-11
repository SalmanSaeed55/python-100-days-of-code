# Dictionaries have 2 parts: Keys and Values
programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
}

print(programming_dictionary["Bug"]) # Fetching from the key of the dictionary

programming_dictionary["Loop"] = "Allowing a piece of code to repeat over and over again." # Adding new items to the dictionary
print(programming_dictionary)

for thing in programming_dictionary:
    print(thing) # Only prints out the keys
    print(programming_dictionary[thing]) # Prints out the values of the keys