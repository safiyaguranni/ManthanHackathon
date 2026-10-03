import pandas as pd
from sklearn.ensemble import RandomForestClassifier

# 1. Mock training data: [Temperature, Pressure] -> Status (0 = Safe, 1 = Risky)
training_data = {
    'Temperature': [30, 85, 32, 90, 29, 88],
    'Pressure': [1.2, 4.5, 1.1, 4.8, 1.0, 4.6],
    'RiskStatus': [0, 1, 0, 1, 0, 1] # 0 = Safe, 1 = Risky Alert
}

df = pd.DataFrame(training_data)

# Separate input features (X) from what we want to predict (y)
X = df[['Temperature', 'Pressure']]
y = df['RiskStatus']

# 2. Initialize and train the Machine Learning model (Random Forest)
model = RandomForestClassifier()
model.fit(X, y)
print("--- Machine Learning Model Trained Successfully! ---")

# 3. Test the model with a brand new live reading
# Let's test a new reading: Temperature = 87°C, Pressure = 4.3
new_live_reading = [[87, 4.3]]
prediction = model.predict(new_live_reading)

if prediction[0] == 1:
    print("Prediction: 🚨 RISK ALERT! System is likely to fail.")
else:
    print("Prediction: ✅ NORMAL. System is safe.")