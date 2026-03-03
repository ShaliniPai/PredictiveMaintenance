
import streamlit as st
import pandas as pd
import joblib
from huggingface_hub import hf_hub_download

# Load trained model from Hugging Face Model Hub
model_path = hf_hub_download(
    repo_id="Shalini94/predictive-maintenance-model",
    filename="best_model.pkl"
)

model = joblib.load(model_path)

st.title("Predictive Maintenance Engine Model")

st.write("""
This application predicts whether an engine requires maintenance 
based on sensor readings.
""")

# Collect user inputs
engine_rpm = st.number_input("Engine RPM", 0, 3000, 800)
lub_oil_pressure = st.number_input("Lub Oil Pressure", 0.0, 10.0, 3.0)
fuel_pressure = st.number_input("Fuel Pressure", 0.0, 25.0, 6.0)
coolant_pressure = st.number_input("Coolant Pressure", 0.0, 10.0, 2.0)
lub_oil_temp = st.number_input("Lub Oil Temperature", 50.0, 120.0, 77.0)
coolant_temp = st.number_input("Coolant Temperature", 50.0, 200.0, 80.0)

# Save inputs into dataframe
input_df = pd.DataFrame([{
    "engine_rpm": engine_rpm,
    "lub_oil_pressure": lub_oil_pressure,
    "fuel_pressure": fuel_pressure,
    "coolant_pressure": coolant_pressure,
    "lub_oil_temp": lub_oil_temp,
    "coolant_temp": coolant_temp
}])

# Predict
if st.button("Predict Engine Condition"):
    prediction = model.predict(input_df)[0]

    if prediction == 1:
        st.error("⚠ Maintenance Required")
    else:
        st.success("✅ Engine Operating Normally")
