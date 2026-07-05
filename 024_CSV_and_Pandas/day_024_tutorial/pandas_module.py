import pandas as pd

data = pd.read_csv("./weather_data.csv")

print(data)

print(data["heat"])

data_dict = data.to_dict()
print(data_dict)

temp_list = data["heat"].tolist()
print(data["heat"].mean())
print(data["heat"].min())
print(data["heat"].max())

print(data[data.day == "Monday"])