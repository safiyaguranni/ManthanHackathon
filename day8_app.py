"""
Project: Real-Time Predictive Analytics & Sensor Monitoring System
Frontend UI: Streamlit Dashboard
Description: Interactive dashboard providing live sensor controls, API communication,
             historical trend visualizations, and raw data previews.
"""

import streamlit as st
import pandas as pd
import requests
import os

# 1. Page Configuration
st.set_page_config(page_title="Advanced Predictive Analytics Dashboard", page_icon="📈", layout="wide")

st.title("📈 Advanced Real-Time Analytics & Sensor Visualizer")
st.write("Welcome to your upgraded hackathon dashboard! This view combines live API predictions with historical data analytics.")

# 2. Load the CSV Data for Visualizations
csv_file_path = "sensor_data.csv"
if os.path.exists(csv_file_path):
    df_history = pd.read_csv(csv_file_path)
else:
    # Fallback dummy data if file is missing
    df_history = pd.DataFrame({
        'Temperature': [30, 85, 31, 91, 29],
        'Pressure': [1.2, 4.5, 1.1, 4.8, 1.0],
        'RiskStatus': [0, 1, 0, 1, 0]
    })

# 3. Sidebar Inputs for Live Simulation
st.sidebar.header("Live Sensor Controls")
temp_input = st.sidebar.slider("Temperature (°C)", min_value=20.0, max_value=100.0, value=30.0)
pressure_input = st.sidebar.slider("Pressure (bar)", min_value=0.5, max_value=6.0, value=1.2)

# 4. Split Screen Layout (Columns)
col1, col2 = st.columns(2)

with col1:
    st.subheader("⚡ Live API Prediction")
    st.metric("Target Temperature", f"{temp_input} °C")
    st.metric("Target Pressure", f"{pressure_input} bar")
    
    if st.button("Fetch Live Prediction from Backend"):
        api_url = f"http://127.0.0.1:8002/predict?temperature={temp_input}&pressure={pressure_input}"
        try:
            response = requests.post(api_url)
            if response.status_code == 200:
                result = response.json()
                if result.get("status") == "Alert":
                    st.error(result.get("message"))
                else:
                    st.success(result.get("message"))
            else:
                st.error("⚠️ Backend error occurred.")
        except Exception as e:
            st.error(f"Connection Error: Make sure FastAPI is running on port 8002! Details: {e}")

with col2:
    st.subheader("📊 Historical Sensor Trends")
    st.write("Visualizing past sensor logs loaded from your dataset:")
    # Render an interactive line chart using Streamlit's built-in tools
    st.line_chart(df_history[['Temperature', 'Pressure']])

# 5. Full-width Data Table Display
st.subheader("📋 Raw Dataset Preview")
st.dataframe(df_history, use_container_width=True)