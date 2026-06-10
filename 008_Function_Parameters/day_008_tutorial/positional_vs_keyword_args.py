# Positional Arguments - specific order, but no need to specify params
def greet(name, location):
    print(f"Hello, {name}!")
    print(f"What is it like in {location}?")


greet("Jeff", "London")

# Keyword arguments - any order specifying param names
greet(location="Berlin", name="Jeff")