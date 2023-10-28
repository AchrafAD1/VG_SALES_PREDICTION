from flask import Flask, render_template, jsonify
from flask_cors import CORS
import csv
import pandas as pd

app = Flask(__name__)
CORS(app)

@app.route('/get_data')
def get_data():
    data = {"keys": [], "records": [], "recordsCount": 0, "keysCount": 0}

    with open('../data1.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        
        headers = next(csv_reader)  # Get the header row
        data["keys"] = headers
        data["keysCount"] = len(headers)
        for row in csv_reader:
            data["records"].append(row)
            data["recordsCount"] += 1
    return jsonify(data)


@app.route('/get_data/moroccan_sales')
def filter_moroccan_data():
    columns_to_keep = ['Name', 'Year_of_Release', 'Genre', 'Publisher', 'MA_Sales', 'Critic_Score', 'Critic_Count', 'User_Score', 'User_Count', 'Developer', 'Rating']

    
    df = pd.read_csv('../data1.csv')
    df = df[columns_to_keep]
    df.to_csv('../data1.csv', index=False)
    

@app.route('/get_data/missing_values')
def delete_missing_values() :
    df = pd.read_csv('../data1.csv')

    # Remove rows with missing values
    df.dropna(inplace=True)

    # Save the cleaned DataFrame back to a CSV file
    df.to_csv('../data1.csv', index=False)


if __name__ == '__main__':
    app.run(debug=True)