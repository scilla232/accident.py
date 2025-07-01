import pandas as pd

# Sample dataset
data = {
    'Speed_Limit': [30, 50, 80, 100, 40, 70],
    'Number_of_Vehicles_Involved': [2, 3, 1, 4, 2, 3],
    'Weather_Condition': [1, 2, 1, 3, 1, 2],           # 1=Clear, 2=Rain, 3=Fog
    'Road_Surface_Condition': [1, 2, 2, 3, 1, 2],      # 1=Dry, 2=Wet, 3=Slippery
    'Light_Condition': [1, 2, 1, 3, 2, 1],             # 1=Day, 2=Night, 3=Dusk
    'Time_of_Day': [8, 13, 20, 22, 18, 6],
    'Driver_Age': [25, 45, 30, 60, 35, 50],
    'Accident_Severity': [1, 2, 3, 3, 2, 1]            # 1=Minor, 2=Moderate, 3=Severe
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Save to CSV file
df.to_csv("accidents_dataset.csv", index=False)

print("Dataset created and saved as accidents_dataset.csv")
