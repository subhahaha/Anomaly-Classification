
import streamlit as st
import joblib
import os

# Load trained model
model_path = os.path.join(os.path.dirname(__file__), "final_model.pkl")
model = joblib.load(model_path)



st.title("Cloud Service Resource Anomaly Detection")

st.write(
    "Enter the cloud service resource metrics to predict "
    "whether the observation is normal or anomalous."
)

# User inputs
response_time = st.number_input(
    "Response Time (ms)",
    min_value=0.0,
    value=2000.0
)

cpu_usage = st.number_input(
    "CPU Usage (%)",
    min_value=0.0,
    max_value=100.0,
    value=50.0
)

memory_usage = st.number_input(
    "Memory Usage (MB)",
    min_value=0.0,
    value=8000.0
)

# Prediction

if st.button("Predict"):
    input_data = [[
        response_time,
        cpu_usage,
        memory_usage
    ]]

    prediction = model.predict(input_data)[0]
    probability = model.predict_proba(input_data)[0][1]

    if prediction == 1:
        st.error("Anomaly Detected")
        st.write("The resource usage pattern appears unusual.")
    else:
        st.success("Normal Observation")
        st.write("The resource usage pattern appears normal.")

    st.write(f"Anomaly Probability: {probability:.2%}")
