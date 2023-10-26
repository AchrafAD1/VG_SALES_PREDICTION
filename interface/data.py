from flask import Flask, render_template, jsonify
from flask_cors import CORS
import csv


app = Flask(__name__)
CORS(app)

@app.route('/get_data')
def get_data():
    data = {"keys": [], "records": []}

    with open('../data1.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        headers = next(csv_reader)  # Get the header row
        data["keys"] = headers

        for row in csv_reader:
            data["records"].append(row)
    return jsonify(data)
if __name__ == '__main__':
    app.run(debug=True)
