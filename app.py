import streamlit as st
import pandas as pd
import pickle
import os

# Function to load the selected model
def load_model(model_name):
    with open(f'{model_name}.pkl', 'rb') as file:
        return pickle.load(file)

# Streamlit UI components
st.title("EV Charging Efficiency Predictor")
st.markdown("""
This web app predicts the efficiency of EV charging based on various factors such as grid availability, weather conditions, battery storage, and renewable energy production. 
Select the appropriate model and input the data to get predictions.
""")

# Model selection dropdown
model_name = st.selectbox('Choose Model', ['lr_model', 'dtr_model']) # 'rfr_model'])

# Define the feature labels based on the selected model
if model_name == 'lr_model': 
    features = [
        'EV Charging Demand (kW)', 'Grid Availability', 'Grid Stability Index',
        'Weather Conditions', 'Battery Storage (kWh)', 'Number of EVs Charging',
        'Peak Demand (kW)', 'Power Outages (hours)', 'Charging Station Capacity (kW)',
        'Effective Charging Capacity (kW)', 'Total Renewable Energy Production (kW)',
        'Renewable Energy Usage (%)'
    ]
    
    
# elif model_name == 'pr_model':
#     features = [
#         'EV Charging Demand (kW)', 'Grid Availability', 'Grid Stability Index',
#         'Weather Conditions', 'Battery Storage (kWh)', 'Number of EVs Charging',
#         'Peak Demand (kW)', 'Power Outages (hours)', 'Charging Station Capacity (kW)',
#         'Effective Charging Capacity (kW)', 'Total Renewable Energy Production (kW)',
#         'Renewable Energy Usage (%)'
#     ]
    
elif model_name == 'dtr_model':
    features = [
        'EV Charging Demand (kW)', 'Grid Availability', 'Grid Stability Index',
        'Weather Conditions', 'Battery Storage (kWh)', 'Number of EVs Charging',
        'Peak Demand (kW)', 'Power Outages (hours)', 'Charging Station Capacity (kW)',
        'Effective Charging Capacity (kW)', 'Solar Energy Production (kW)',
        'Wind Energy Production (kW)', 'Renewable Energy Usage (%)'
    ]
elif model_name == 'rfr_model':
    features = [
        'EV Charging Demand (kW)', 'Solar Energy Production (kW)', 'Wind Energy Production (kW)',
        'Electricity Price ($/kWh)', 'Grid Availability', 'Weather Conditions', 'Battery Storage (kWh)',
        'Charging Station Capacity (kW)', 'EV Charging Efficiency (%)', 'Number of EVs Charging',
        'Peak Demand (kW)', 'Renewable Energy Usage (%)', 'Grid Stability Index', 'Carbon Emissions (kgCO2/kWh)',
        'Power Outages (hours)', 'Energy Savings ($)', 'Total Renewable Energy Production (kW)',
        'Effective Charging Capacity (kW)', 'Adjusted Charging Demand (kW)'
    ]

# Load the selected model
model = load_model(model_name)

# Input fields for EV charging prediction
st.header("Enter the following details to predict EV Charging Efficiency")

# Create dynamic input fields based on the selected features
input_values = []
for feature in features:
    value = st.number_input(feature, min_value=0.0)
    input_values.append(value)

# Predict button
if st.button("Predict Efficiency"):
    # Convert inputs to DataFrame
    input_df = pd.DataFrame([input_values], columns=features)
    
    # Make prediction
    prediction = model.predict(input_df)
    st.success(f"Predicted EV Charging Efficiency: {prediction[0]:.2f}%")

# Add footer with additional information
st.markdown("""
---
*This model predicts the efficiency of EV charging based on multiple factors. The accuracy of predictions depends on the selected model and the quality of the input data provided.*
""")
