capitals = {
    "France": "Paris",
    "Germany": "Berlin",
}

travel_log = {
    "France": ["Paris", "Dunkirk", "Lille"], # Nested lists within a dictionary
    "Germany": ["Berlin", "Munich", "Augsburg"],
}

print(travel_log["France"]) # Output: ['Paris', 'Dunkirk', 'Lille'] - list
print(travel_log["France"][2]) # Output: 'Lille' - string

# Nesting lists in lists
nested_list = ["0", "1", ["c", "d"]]

print(nested_list[2]) # Output: ['c', 'd'] - list
print(nested_list[2][0]) # Output: 'c' - string

