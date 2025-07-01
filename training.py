import pandas as pd

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import pickle

# Load dataset
df = pd.read_csv("accidents_dataset.csv")

# Separate input (X) and output (y)
X = df.drop("Accident_Severity", axis=1)
y = df["Accident_Severity"]

# Split into training and testing
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize and train the model
model = LinearRegression()
model.fit(X_train, y_train)

# Save the model to a file
with open("accident_severity_model.pkl", "wb") as file:
    pickle.dump(model, file)

print("Model trained and saved as accident_severity_model.pkl")
