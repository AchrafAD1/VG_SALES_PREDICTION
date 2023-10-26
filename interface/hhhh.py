import pandas as pd
import random

# Load the CSV file into a DataFrame
csv_file = "../Cleaned Data 2.csv"


def hhhh ():
    df = pd.read_csv(csv_file)
    # Generate a new row with missing values
    new_row = {
        "Name": "New Game",
        "Year_of_Release": random.randint(1990, 2023),
        "Genre": "Random Genre",
        "Publisher": "Random Publisher",
        "NA_Sales": [random.uniform(0,2), None, None, None, None, None][random.randint(0, 1)],
        "EU_Sales": [random.uniform(0,2),None,None, None, None, None, None][random.randint(0, 1)],
        "JP_Sales": [random.uniform(0,2),None,None, None, None, None, None][random.randint(0, 1)],
        "Other_Sales": [random.uniform(0,2),None,None, None, None, None, None][random.randint(0, 1)],
        "Global_Sales": [random.uniform(0,2),None,None, None, None, None, None][random.randint(0, 1)],
        "Critic_Score":  [random.randint(0, 100),None, None, None, None, None][random.randint(0, 1)],
        "Critic_Count": [random.randint(0, 100),None, None, None, None, None][random.randint(0, 1)],
        "User_Score": [random.uniform(0,2),None][random.randint(0, 1)],
        "User_Count": [random.randint(0, 1000),None, None, None, None, None][random.randint(0, 1)],
        "Developer": "Random Developer",
        "Rating": "Random Rating"
    }

    # Select a random position to insert the new row
    insert_pos = random.randint(2, len(df))

    # Insert the new row into the DataFrame
    df = pd.concat([df.iloc[:insert_pos], pd.DataFrame([new_row]), df.iloc[insert_pos:]]).reset_index(drop=True)

    # Save the modified DataFrame back to the CSV file
    df.to_csv(csv_file, index=False)

for i in range(3000):
    hhhh()
