import pandas as pd
import numpy as np
import pickle
import streamlit as st
from PIL import Image

# loading in the model to predict on the data
pickle_in = open('random_forest_modelv1.pkl', 'rb')
classifier = pickle.load(pickle_in)
def app():

def welcome():
    return 'welcome all'


# defining the function which will make the prediction using
# the data which the user inputs
def prediction(Patient_Name, Gender, Age, BMI, FBG, TWO_HOUR_POSTPRANADIAL_GLUCOSE, Hba1c, Family_History, Urine_Microalbumin, Urine_Glucose, Urine_Ketones,
Lipid_Profile, Physical_Activity, Diabetic_Status):
    prediction = classifier.predict(
        [[Patient_Name, Gender, Age, BMI, FBG, TWO_HOUR_POSTPRANADIAL_GLUCOSE, Hba1c, Family_History, Urine_Microalbumin, Urine_Glucose, Urine_Ketones,
Lipid_Profile, Physical_Activity, Diabetic_Status]])
    print(prediction)
    return prediction

#Patient ID,Patient Name,"Gender (0: Male, 1: Female)",Age,BMI,FBG,
#2 HOUR POSTPRANDIAL GLUCOSE,HbA1c,"Family History (0: No, 1: Yes)",
#Urine Microalbumin,"Urine Glucose (0: Normal, 1: Abnormal)","Urine Ketones (0: Normal, 1: Abnormal)",
#Lipid Profile (Normal/Abnormal),Physical Activity,Date,Referred By,
#Lab,"Diabetes Status (0: Non-Diabetic, 1: Pre-Diabetic, 2: Diabetic)",Systolic BP,Diastolic BP
# this is the main function in which we define our webpage
def main():
    # giving the webpage a title
    st.title("Diabetes Prediction")

    # here we define some of the front end elements of the web page like
    # the font and background color, the padding and the text to be displayed
    html_temp = """ 
    <div style ="background-color:yellow;padding:13px"> 
    <h1 style ="color:black;text-align:center;">Diabetes Prediction System </h1> 
    </div> 
    """

    # this line allows us to display the front end aspects we have
    # defined in the above code
    st.markdown(html_temp, unsafe_allow_html=True)

    # the following lines create text boxes in which the user can enter
    # the data required to make the prediction
    Patient = st.text_input("Enter Your name")
    Gender  = st.radio("Select Gender: ", ('Male', 'Female'))
    if (Gender == 'Male'):
        st.success("Male")
    else:
        st.success("Female")

    Age = st.slider("Select the level", 1, 110)
    BMI = st.slider("Select the level", 1, 5)
    FBG = st.slider("Select the level", 1, 5)
    TWO_HOUR_POSTPRANADIAL_GLUCOSE = st.slider("Select the level", 1, 5)
    Family_History = st.slider("Select the level", 1, 5)
    Urine_Microalbumin= st.slider("Select the level", 1, 5)
    Urine_Glucose = st.slider("Select the level", 1, 5)
    Urine_Ketones = st.slider("Select the level", 1, 5)
    Lipid_Profile = st.slider("Select the level", 1,5)
    Physical_Activity = st.radio("Select Activity: ", ('Yes','No'))
    if (family_history == 'Yes'):
        st.success("Yes")
    else:
        st.success("No")
    result = ""

    # the below line ensures that when the button called 'Predict' is clicked,
    # the prediction function defined above is called to make the prediction
    # and store it in the variable result
    if st.button("Predict"):
        result = prediction(sepal_length, sepal_width, petal_length, petal_width)
    st.success('The output is {}'.format(result))


if __name__ == '__main__':
    main()

#Patient ID,Patient Name,"Gender (0: Male, 1: Female)",Age,BMI,FBG,
#2 HOUR POSTPRANDIAL GLUCOSE,HbA1c,"Family History (0: No, 1: Yes)",
#Urine Microalbumin,"Urine Glucose (0: Normal, 1: Abnormal)","Urine Ketones (0: Normal, 1: Abnormal)",
#Lipid Profile (Normal/Abnormal),Physical Activity,Date,Referred By,
#Lab,"Diabetes Status (0: Non-Diabetic, 1: Pre-Diabetic, 2: Diabetic)",Systolic BP,Diastolic BP
