import pandas as pd

# Load the CSV file into a DataFrame
df = pd.read_csv('C:/Users/namit/mini_project/World Happiness Report.csv')

# Print all column names
print("Column Names:")
for column in df.columns:
    print(column)
