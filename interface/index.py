# Import necessary libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import StandardScaler, LabelEncoder, OneHotEncoder
from sklearn.compose import ColumnTransformer

# Load the dataset
data = pd.read_csv('../Cleaned Data 2.csv')

# Data Preprocessing

# Handle missing values (if any)
data.dropna(inplace=True)

# One-hot encode categorical variables (Genre and Publisher)
encoder = LabelEncoder()
data['Genre'] = encoder.fit_transform(data['Genre'])
data['Publisher'] = encoder.fit_transform(data['Publisher'])

# Define features (independent variables) and target (dependent variable)
features = ['Year_of_Release', 'Genre', 'Publisher', 'NA_Sales', 'JP_Sales', 'Other_Sales', 'Global_Sales', 'Critic_Score', 'Critic_Count', 'User_Score', 'User_Count']
target = ['EU_Sales']

# Split the data into a training set and a testing set
X = data[features]
y = data[target]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Normalize or scale numerical features (if needed)
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Train the Linear Regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
rmse = mse**0.5
r2 = r2_score(y_test, y_pred)

print(f"Mean Squared Error: {mse}")
print(f"Root Mean Squared Error: {rmse}")
print(f"R-squared (R2) Score: {r2}")

# Predict the game with the highest European sales in 2017
# Filter the dataset for games released in or before 2017
games_2017 = data[data['Year_of_Release'] <= 2017]

# Use the trained model to predict European sales for these games
X_2017 = games_2017[features]
X_2017 = scaler.transform(X_2017)
predicted_sales_2017 = model.predict(X_2017)

# Find the game with the highest predicted European sales
max_sales_index = predicted_sales_2017.argmax()
game_with_highest_sales = games_2017.iloc[max_sales_index]
print("Game with the highest predicted European sales in 2017:")
print(game_with_highest_sales)
