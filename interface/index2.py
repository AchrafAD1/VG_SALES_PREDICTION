# Import necessary libraries
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler, LabelEncoder

# Load the dataset
data = pd.read_csv('../data1.csv')

# Handle missing values (if any)
data.dropna(inplace=True)

# One-hot encode categorical variables (Genre and Publisher)
encoder = LabelEncoder()
data['Genre'] = encoder.fit_transform(data['Genre'])
data['Publisher'] = encoder.fit_transform(data['Publisher'])

# Define features (independent variables) and target (dependent variable)
features = ['Genre', 'Publisher', 'Critic_Score', 'Critic_Count', 'User_Score', 'User_Count']
target = ['EU_Sales']

# Normalize or scale numerical features (if needed)
scaler = StandardScaler()
X = data[features]
y = data[target]
X = scaler.fit_transform(X)

# Train the Linear Regression model
model = LinearRegression()
model.fit(X, y)

# ... (previous code) ...

# Function to make predictions for a new game
def predict_game_sales(genre, publisher, critic_score, critic_count, user_score, user_count):

    
    # Check if the user input for genre and publisher is in the label encoding
    if genre not in encoder.classes_:
        print(f"Invalid genre: {genre}. Please enter a valid genre.")
        return
    if publisher not in encoder.classes_:
        print(f"Invalid publisher: {publisher}. Please enter a valid publisher.")
        return

    # Encode genre and publisher
    genre_encoded = encoder.transform([genre])[0]
    publisher_encoded = encoder.transform([publisher])[0]

    # Create input data for prediction
    input_data = [[genre_encoded, publisher_encoded, critic_score, critic_count, user_score, user_count]]

    # Make predictions
    predicted_sales = model.predict(input_data)

    return predicted_sales[0][0]

# User input for game details
genre = input("Enter the game's genre: ")
publisher = input("Enter the game's publisher: ")

# Check if the user input for genre and publisher is valid
if genre not in encoder.classes_:
    print(f"Invalid genre: {genre}. Please enter a valid genre.")
elif publisher not in encoder.classes_:
    print(f"Invalid publisher: {publisher}. Please enter a valid publisher.")
else:
    # User input for other parameters
    critic_score = float(input("Enter the critic score: "))
    critic_count = float(input("Enter the critic count: "))
    user_score = float(input("Enter the user score:"))
    
    # Validate user input for user_count
    while True:
        user_count_input = input("Enter the user count: ")
        try:
            user_count = float(user_count_input)
            break
        except ValueError:
            print("Invalid input for user count. Please enter a numeric value.")

    # Predict the game sales
    predicted_sales = predict_game_sales(genre, publisher, critic_score, critic_count, user_score, user_count)

    if predicted_sales is not None:
        print(f"Predicted European Sales for the game: {predicted_sales:.2f} million copies")
