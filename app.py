import streamlit as st
import pickle
import numpy as np

# Load model
with open("model1.pkl", "rb") as file:
    model = pickle.load(file)

st.title("Insurance Cost Prediction App")

age = st.number_input("Age", min_value=1, max_value=100, value=25)
sex = st.selectbox("Sex", ["male", "female"])
bmi = st.number_input("BMI", min_value=10.0, max_value=50.0, value=22.5)
children = st.number_input("Children", min_value=0, max_value=10, value=0)
smoker = st.selectbox("Smoker", ["yes", "no"])
region = st.selectbox("Region", ["southwest", "southeast", "northwest", "northeast"])

# Convert categorical to numeric (must match your training encoding!)
sex = 1 if sex == "male" else 0
smoker = 1 if smoker == "yes" else 0
region_dict = {"southwest":0, "southeast":1, "northwest":2, "northeast":3}
region = region_dict[region]

# Prepare input
input_data = np.array([[age, sex, bmi, children, smoker, region]])

if st.button("Predict Insurance Cost"):
    prediction = model.predict(input_data)
    st.success(f"Estimated Insurance Cost: ${prediction[0]:.2f}")