import pandas as pd

# Define the path to the CSV file
csv_file_path = "C:/Users/namit/mini_project/World Happiness Report.csv"

# Load the dataset from the CSV file into a Pandas DataFrame
df = pd.read_csv(csv_file_path)

# Display the first few rows of the DataFrame to verify the data
print(df.head())
