import pandas as pd
from flask import Flask, jsonify, render_template
from flask_cors import CORS  # Import the CORS extension

app = Flask(__name__)

cors = CORS(app, resources={r"/get_data": {"origins": "*"}})

@app.route('/get_data', methods=['GET'])
def get_data():
    # Load your dataset into a DataFrame
    df = pd.read_csv('../vgsales.csv')

    # Encode categorical variables using one-hot encoding
    df = pd.get_dummies(df, columns=['Platform', 'Genre', 'Publisher'])

    # Calculate your desired results
    total_sales = df[df['Year'].isin(list(range(2015, 2023)))]['EU_Sales'].sum()
    
    #First 

    # Create a dictionary to hold the results
    result = {"total_sales": total_sales,}

    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
