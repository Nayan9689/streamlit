import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Load the dataset
@st.cache
def load_data():
    return pd.read_csv("pages/finalv1_data.csv")

data = load_data()

# Define input fields
st.sidebar.header('User Input Features')

def user_input_features():
    gender = st.sidebar.selectbox('Gender', [0, 1])
    age = st.sidebar.slider('Age', 1, 100, 25)
    bmi = st.sidebar.slider('BMI', 10.0, 50.0, 25.0)
    fbg = st.sidebar.slider('Fasting Blood Glucose (mg/dL)', 50, 300, 100)
    pp2g = st.sidebar.slider('2 Hour Postprandial Glucose (mg/dL)', 50, 300, 150)
    hba1c = st.sidebar.slider('HbA1c (%)', 4.0, 15.0, 6.0)
    family_history = st.sidebar.selectbox('Family History', [0, 1])
    urine_microalbumin = st.sidebar.slider('Urine Microalbumin (mg/L)', 0, 300, 0)
    urine_glucose = st.sidebar.selectbox('Urine Glucose', [0, 1])
    urine_ketones = st.sidebar.selectbox('Urine Ketones', [0, 1])
    lipid_profile = st.sidebar.radio('Lipid Profile (Normal/Abnormal)', ['Normal', 'Abnormal'])
    physical_activity = st.sidebar.slider('Physical Activity (hrs/week)', 0, 50, 0)
    systolic_bp = st.sidebar.slider('Systolic Blood Pressure (mmHg)', 80, 200, 120)
    diastolic_bp = st.sidebar.slider('Diastolic Blood Pressure (mmHg)', 50, 150, 80)
    return gender, age, bmi, fbg, pp2g, hba1c, family_history, urine_microalbumin, urine_glucose, urine_ketones, lipid_profile, physical_activity, systolic_bp, diastolic_bp

gender, age, bmi, fbg, pp2g, hba1c, family_history, urine_microalbumin, urine_glucose, urine_ketones, lipid_profile, physical_activity, systolic_bp, diastolic_bp = user_input_features()

# Preprocess input data
# Convert categorical variables to numerical, scale features, etc.

# Load or train your model
# For example, if you have a pre-trained RandomForestClassifier:
model = RandomForestClassifier()
X = data.drop(columns=['Diabetes Status (0: Non-Diabetic, 1: Pre-Diabetic, 2: Diabetic'])
y = data['Diabetes Status (0: Non-Diabetic, 1: Pre-Diabetic, 2: Diabetic']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model.fit(X_train, y_train)

# Make predictions
prediction = model.predict([[gender, age, bmi, fbg, pp2g, hba1c, family_history, urine_microalbumin, urine_glucose, urine_ketones, lipid_profile, physical_activity, systolic_bp, diastolic_bp]])

# Display prediction
st.subheader('Prediction')
if prediction[0] == 0:
    st.write('Non-Diabetic')
elif prediction[0] == 1:
    st.write('Pre-Diabetic')
else:
    st.write('Diabetic')
