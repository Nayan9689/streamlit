import streamlit as st
import pandas as pd
import pickle

# Load the trained model
with open('random_forest_modelv1.pkl', 'rb') as file:
    model = pickle.load(file)


# Function to preprocess input data
def preprocess_input(input_data):
    # Preprocessing steps go here
    # For simplicity, let's assume input_data is already preprocessed
    return input_data


# Function to make predictions
def predict(input_data):
    # Preprocess the input data
    input_data_processed = preprocess_input(input_data)

    # Make predictions
    prediction = model.predict(input_data_processed)

    return prediction


# Streamlit UI
def main():
    st.title("Diabetes Prediction System")
    st.markdown("Enter patient information to predict diabetes status.")

    # Input form
    with st.form("input_form"):
        st.header("Patient Information")

        # Define input fields
        patient_id = st.text_input("Patient ID")
        patient_name = st.text_input("Patient Name")
        gender = st.text_input("Gender", ["Male", "Female"])
        age = st.number_input("Age", min_value=0, max_value=150, value=30)
        bmi = st.number_input("BMI", min_value=0.0, max_value=100.0, value=25.0)
        fbg = st.number_input("Fasting Blood Glucose", min_value=0, max_value=1000, value=100)
        # Add other input fields similarly

        # Submit button
        submitted = st.form_submit_button("Predict")

    if submitted:
        # Prepare input data
        input_data = {
            "Patient ID": patient_id,
            "Patient Name": patient_name,
            "Gender": 0 if gender == "Male" else 1,  # Convert gender to 0 for Male, 1 for Female
            "Age": age,
            "BMI": bmi,
            "FBG": fbg,
            # Add other input fields similarly
        }

        # Make prediction
        prediction = predict(input_data)

        # Display prediction
        st.subheader("Prediction")
        st.write(f"The predicted diabetes status is: {prediction}")


if __name__ == "__main__":
    main()
