enemies = 1


def increase_enemies():
    enemies = 2
    print(f"Enemies inside function: {enemies}")


increase_enemies()
print(f"Enemies outside function: {enemies}")


# Local scope - a local variable in a function is only accessible inside the function where it is defined. It cannot be accessed outside of that function.
def drink_potion():
    potion_strength = 2
    print(potion_strength)


drink_potion()
# print(potion_strength)  - This will raise an error because potion_strength is not defined in the global scope

# Global scope
player_health = 10 # This lies in the global scope of the program


def drink_potion():
    potion_strength = 2
    print(player_health) # works because player health is in the global scope

drink_potion()
