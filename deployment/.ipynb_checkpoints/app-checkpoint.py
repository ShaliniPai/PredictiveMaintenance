import os
import streamlit as st
import pandas as pd
from joblib import load
from huggingface_hub import hf_hub_download

st.title("Predictive Maintenance Engine Model")

# ------------------------------
# Model Loading Logic
# ------------------------------

if os.environ.get("LOCAL_TESTING"):
    model = load("../data/best_model.pkl")
else:
    model_path = hf_hub_download(
        repo_id="Shalini94/PredictiveMaintenance",  # ← MUST match your model repo exactly
        filename="best_model.pkl"
    )
    model = load(model_path)

st.subheader("Enter Engine Sensor Values")

engine_rpm = st.number_input("Engine RPM", value=800)
lub_oil_pressure = st.number_input("Lub Oil Pressure", value=3.0)
fuel_pressure = st.number_input("Fuel Pressure", value=6.0)
coolant_pressure = st.number_input("Coolant Pressure", value=2.0)
lub_oil_temp = st.number_input("Lub Oil Temperature", value=77.0)
coolant_temp = st.number_input("Coolant Temperature", value=80.0)

if st.button("Predict Engine Condition"):

    input_df = pd.DataFrame([{
        "engine_rpm": engine_rpm,
        "lub_oil_pressure": lub_oil_pressure,
        "fuel_pressure": fuel_pressure,
        "coolant_pressure": coolant_pressure,
        "lub_oil_temp": lub_oil_temp,
        "coolant_temp": coolant_temp
    }])

    prediction = model.predict(input_df)[0]

    if prediction == 1:
        st.error("Maintenance Required")
    else:
        st.success("Normal Operation")