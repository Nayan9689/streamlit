import pandas as pd
import streamlit as st


df = pd.read_csv('finalv1_data.csv')
st.title("Admin Pannel")
st.dataframe(df)
clicked = st.button("Edit")
clicked = st.button("Delete")
st.sidebar.success("Welcome to Admin Panel")
refresh = st.toggle("Refresh")
st.sidebar.write("hi")
st.sidebar.button("login")
st.sidebar.button("Sign Up")
st.sidebar.button("Diabetes prediction Form")
st.sidebar.button("Report Generation")
st.sidebar.button("Signout")

