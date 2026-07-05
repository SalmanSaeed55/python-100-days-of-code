import pandas as pd

data_dict = {
    "students": ["Jack", "John", "Joe", "Harry"],
    "scores": [45, 34, 56, 36]
}

df = pd.DataFrame(data_dict)
df.to_csv("students.csv")