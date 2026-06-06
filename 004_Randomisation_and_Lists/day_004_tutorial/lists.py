import random

states_of_america = ["Washington", "Texas", "Louisiana"]

print(states_of_america[2])
print(states_of_america[-1])

states_of_america.append("New York")

print(states_of_america)

# Coding Challenge
names = ["John", "Jack", "Harry", "Sam", "Tyler", "Henry", "Ben"]

## Option 1
print(random.choice(names))

choice = random.randint(0, len(names) - 1)
print(names[choice])