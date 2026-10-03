"""
Project: Real-Time Predictive Analytics & Sensor Monitoring System
Backend API: FastAPI
Description: Loads historical sensor data, trains a Random Forest classifier, 
             and serves real-time failure predictions via HTTP POST endpoints.
"""

from fastapi import FastAPI
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import os

# 1. Initialize FastAPI app
app = FastAPI(title="CSV-Powered Predictive Analytics API")

# 2. Load the dataset using Pandas when the app starts
csv_file_path = "sensor_data.csv"

if os.path.exists(csv_file_path):
    df = pd.read_csv(csv_file_path)
    print("Successfully loaded CSV dataset!")
else:
    # Fallback backup data if CSV isn't found
    df = pd.DataFrame({
        'Temperature': [30, 90],
        'Pressure': [1.2, 4.8],
        'RiskStatus': [0, 1]
    })

# 3. Train the model using the real CSV data
X = df[['Temperature', 'Pressure']]
y = df['RiskStatus']

model = RandomForestClassifier()
model.fit(X, y)

# 4. Define the prediction endpoint
@app.post("/predict")
def predict_risk(temperature: float, pressure: float):
    prediction = model.predict([[temperature, pressure]])
    
    if prediction[0] == 1:
        return {"status": "Alert", "message": "🚨 RISK: System failure predicted from CSV data!"}
    else:
        return {"status": "Normal", "message": "✅ System is safe based on historical trends."}