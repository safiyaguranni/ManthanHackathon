import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

# 1. Page Configuration
st.set_page_config(page_title="Real-Time Predictive Analytics", page_icon="📊", layout="centered")

st.title("🚨 Real-Time Risk & Predictive Analytics Dashboard")
st.write("Welcome to your Manthan hackathon project interface! Adjust the live sensor metrics below to test predictions.")

# 2. Train the model behind the scenes
@st.cache_resource
def load_trained_model():
    training_data = {
        'Temperature': [30, 85, 32, 90, 29, 88],
        'Pressure': [1.2, 4.5, 1.1, 4.8, 1.0, 4.6],
        'RiskStatus': [0, 1, 0, 1, 0, 1]
    }
    df = pd.DataFrame(training_data)
    X = df[['Temperature', 'Pressure']]
    y = df['RiskStatus']
    model = RandomForestClassifier()
    model.fit(X, y)
    return model

model = load_trained_model()

# 3. Sidebar Inputs for Live Simulation
st.sidebar.header("Live Sensor Controls")
temp_input = st.sidebar.slider("Temperature (°C)", min_value=20.0, max_value=100.0, value=30.0)
pressure_input = st.sidebar.slider("Pressure (bar)", min_value=0.5, max_value=6.0, value=1.2)

# 4. Main Panel Display
st.subheader("Current Live Reading")
col1, col2 = st.columns(2)
col1.metric("Temperature", f"{temp_input} °C")
col2.metric("Pressure", f"{pressure_input} bar")

# 5. Prediction Trigger Button
if st.button("Run Real-Time Prediction"):
    prediction = model.predict([[temp_input, pressure_input]])
    
    if prediction[0] == 1:
        st.error("🚨 RISK ALERT! System is likely to fail! Immediate action required.")
    else:
        st.success("✅ SYSTEM NORMAL. Operating within safe parameters.")