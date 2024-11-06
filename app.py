import streamlit as st
import pandas as pd
import pickle
import os
import subprocess

try:
    import sklearn
except ImportError:
    subprocess.check_call(["pip", "install", "scikit-learn"])
    import sklearn  
try:
    with open('lr_model.pkl', 'rb') as file:
        lr_model = pickle.load(file)
    st.write("Model loaded successfully!")
except Exception as e:
    st.error(f"An error occurred while loading the model: {e}")
# Define the Streamlit app
st.title("EV Charging Efficiency Predictor")

# Input fields
ev_demand = st.number_input('EV Charging Demand (kW)')
grid_availability = st.number_input('Grid Availability')
grid_stability = st.number_input('Grid Stability Index')
weather_conditions = st.number_input('Weather Conditions')
battery_storage = st.number_input('Battery Storage (kWh)')
number_of_evs = st.number_input('Number of EVs Charging')
peak_demand = st.number_input('Peak Demand (kW)')
power_outages = st.number_input('Power Outages (hours)')
charging_station_capacity = st.number_input('Charging Station Capacity (kW)')
effective_charging_capacity = st.number_input('Effective Charging Capacity (kW)')
total_renewable_energy_production = st.number_input('Total Renewable Energy Production (kW)')
renewable_energy_usage = st.number_input('Renewable Energy Usage (%)')

# Prediction
if st.button("Predict Efficiency"):
    inputs = [[
        ev_demand, grid_availability, grid_stability, weather_conditions,
        battery_storage, number_of_evs, peak_demand, power_outages,
        charging_station_capacity, effective_charging_capacity,
        total_renewable_energy_production, renewable_energy_usage
    ]]
    
    # Convert inputs to DataFrame
    input_df = pd.DataFrame(inputs, columns=[
        'EV Charging Demand (kW)', 'Grid Availability', 'Grid Stability Index',
        'Weather Conditions', 'Battery Storage (kWh)', 'Number of EVs Charging',
        'Peak Demand (kW)', 'Power Outages (hours)', 'Charging Station Capacity (kW)',
        'Effective Charging Capacity (kW)', 'Total Renewable Energy Production (kW)',
        'Renewable Energy Usage (%)'
    ])
    
    # Make prediction
    prediction = lr_model.predict(input_df)
    st.success(f"Predicted EV Charging Efficiency: {prediction[0]:.2f}%")
