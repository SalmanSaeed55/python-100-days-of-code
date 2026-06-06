import random
import my_module # importing your own module

num = random.randint(1, 10) # Using the random module to generate a random integer between 1 and 10
print(num)

print(my_module.favourite_number) # dot notation to retrieve something from your own module

random_number = random.random() # random number between 0 and 1
print(random_number)

random_float = random.uniform(1, 10) # random floating point number between 1 and 19
print(random_float)
