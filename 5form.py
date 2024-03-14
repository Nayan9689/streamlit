import streamlit as st
from joblib import load

# Load the model
model = load('C:/Users/Dell/Desktop/streamlit/pages/random_forest_model.joblib')

with st.form("Diabetes Prediction System Details"):
    st.title('Welcome to Diabetes Prediction System')
    name = st.text_input("Enter Your Name")
    gender = st.number_input("Gender", 0,1)
    st.text("Gender 0: Male, 1: Female")
    age = st.slider("Select Your Age", 0, 150)
    bmi = st.number_input("BMI", 1,150)
    fbg = st.number_input("FBG")
    postprandial_glucose = st.number_input("2 Hour Postprandial Glucose")
    hba1c = st.number_input("Hba1c")
    st.text("Family History 1:Yes, 0:No")
    family_history = st.number_input("Family History", 0,1)
    urine_microalbumin = st.number_input("Urine Microalbumin", 0,300)
    st.text("Urine Glucose 0:Normal, 1:Abnormal")
    urine_glucose = st.number_input("Urine Glucose ", 0,1)
    st.text("Urine Ketonese 0:Normal, 1:Abnormal")
    urine_ketones = st.number_input("Urine Ketones ", 0,1)
    st.text("Lipid Profile 0:Normal, 1:Abnormal")
    lipid_profile = st.number_input("Lipid Profile ", 0,1)
    st.text("Physical Activity 1:Yes 0:No 2:Someday")
    physical_activity = st.number_input("Physical Activity",0,2)
    systolic_bp = st.number_input("Systolic BP")
    diastolic_bp = st.number_input("Diastolic BP")

    submitted = st.form_submit_button("Predict")

if submitted:
    # Prepare the input data
    user_input = [age, bmi, fbg, postprandial_glucose, hba1c, urine_microalbumin, urine_glucose, urine_ketones, lipid_profile, systolic_bp, diastolic_bp]


    # Make prediction
    prediction = model.predict([user_input])

    st.write(f"Hello {name}, based on the provided information, the prediction result is: {prediction[0]}")
