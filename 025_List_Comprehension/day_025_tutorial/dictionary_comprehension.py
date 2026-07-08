import random
names = ["Alice", "Bob", "Charlie", "David"]

scores = {name: random.randint(1, 100) for name in names}
print(scores)