# Load the trained model
import pandas as pd
import pickle

with open("accident_severity_model.pkl", "rb") as file:
    model = pickle.load(file)

# Create a test input
input_data = pd.DataFrame({
    'Speed_Limit': [90],
    'Number_of_Vehicles_Involved': [2],
    'Weather_Condition': [2],
    'Road_Surface_Condition': [2],
    'Light_Condition': [1],
    'Time_of_Day': [15],
    'Driver_Age': [28]
})

# Make prediction
prediction = model.predict(input_data)
print("Predicted Accident Severity:", round(prediction[0], 2))
