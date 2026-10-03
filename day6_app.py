import streamlit as st
import requests

# 1. Page Configuration
st.set_page_config(page_title="Production-Grade Predictive Dashboard", page_icon="⚡", layout="centered")

st.title("⚡ Connected Real-Time Analytics Dashboard")
st.write("This dashboard communicates directly with your **FastAPI backend** running on localhost!")

# 2. Sidebar Inputs for Live Simulation
st.sidebar.header("Live Sensor Controls")
temp_input = st.sidebar.slider("Temperature (°C)", min_value=20.0, max_value=100.0, value=30.0)
pressure_input = st.sidebar.slider("Pressure (bar)", min_value=0.5, max_value=6.0, value=1.2)

# 3. Main Panel Display
st.subheader("Current Live Reading")
col1, col2 = st.columns(2)
col1.metric("Temperature", f"{temp_input} °C")
col2.metric("Pressure", f"{pressure_input} bar")

# 4. Prediction Trigger Button (Calling FastAPI Backend)
# 4. Prediction Trigger Button (Calling FastAPI Backend)
if st.button("Fetch Prediction from API"):
    # FastAPI endpoint URL (using port 8001 as we updated earlier)
    api_url = f"http://127.0.0.1:8002/predict?temperature={temp_input}&pressure={pressure_input}"
    
    try:
        # Send POST request to FastAPI backend
        response = requests.post(api_url)
        
        # Display raw response code for debugging
        st.write(f"API Response Status Code: {response.status_code}")
        
        if response.status_code == 200:
            result = response.json()
            status = result.get("status")
            message = result.get("message")
            
            if status == "Alert":
                st.error(message)
            else:
                st.success(message)
        else:
            st.error(f"⚠️ Server returned an error: {response.text}")
            
    except Exception as e:
        st.error(f"Connection Error: Is your FastAPI server running on port 8001? Details: {e}")