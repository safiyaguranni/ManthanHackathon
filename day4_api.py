from fastapi import FastAPI
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

# 1. Initialize FastAPI app
app = FastAPI(title="Real-Time Predictive Analytics API")

# 2. Train our model right when the app starts up
training_data = {
    'Temperature': [30, 85, 32, 90, 29, 88],
    'Pressure': [1.2, 4.5, 1.1, 4.8, 1.0, 4.6],
    'RiskStatus': [0, 1, 0, 1, 0, 1]  # 0 = Safe, 1 = Risky
}
df = pd.DataFrame(training_data)
X = df[['Temperature', 'Pressure']]
y = df['RiskStatus']

model = RandomForestClassifier()
model.fit(X, y)

# 3. Define a web route (Endpoint) for predictions
@app.post("/predict")
def predict_risk(temperature: float, pressure: float):
    # Make prediction using the live inputs sent to the API
    prediction = model.predict([[temperature, pressure]])
    
    if prediction[0] == 1:
        return {"status": "Alert", "message": "🚨 RISK: System is likely to fail!"}
    else:
        return {"status": "Normal", "message": "✅ System is safe."}