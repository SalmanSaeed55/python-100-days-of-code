import csv

with open("weather_data.csv") as csv_file:
    csv_reader = csv.reader(csv_file)
    temps = []
    for row in csv_reader:
        if row[1] == "heat":
            pass
        else:
            temps.append(row[1])

print(temps)

