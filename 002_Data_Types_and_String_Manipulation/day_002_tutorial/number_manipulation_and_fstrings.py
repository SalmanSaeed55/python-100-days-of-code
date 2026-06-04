bmi = 75 / (1.82 ** 2)
print(bmi)

print(int(bmi)) # Convert to integer, will round down
print(round(bmi)) # Round to nearest whole number

print(round(bmi, 2)) # Round to 2 decimal places

print()

# Shorthand reassignment operators
score = 0
score += 5
print(score)
score -= 2
print(score)


# f-strings
score = 0
height = 1.8
is_winning = True

print(f"Your score is {score}\nYour height is {height}\nAre you winning? {is_winning}")

