import pandas as pd

# Read the CSV file
input_file = 'data1.csv'
df = pd.read_csv(input_file)

# Define the columns to be rounded
sales_columns = ['MA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales', 'Global_Sales']

# Round the values in the specified columns to two decimal places
df[sales_columns] = df[sales_columns].round(2)

# Write the modified data to a new CSV file
output_file = 'output.csv'
df.to_csv(output_file, index=False)

print("Values with more than two digits after the decimal point have been rounded and saved to", output_file)
