print("Welcome to the tip calculator.")

bill = float(input("What is the total bill? \t£"))
tip = int(input("How much would you like to tip? 10%, 12% or 15%?\t"))
people = int(input("How many people to split the bill?\t"))

total_bill = bill + (bill * (tip / 100))
total_per_person = total_bill / people

print(f"Each person should pay:\t£{round(total_per_person, 2)}")
