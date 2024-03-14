import streamlit as st
st.set_page_config(page_title="🚥Sign UP")
st.text("Welcome To Sign Up")


def login():
    username = st.text_input("Enter Your Name")
    password = st.text_input("Enter Your Password")
    valid_users = ['user1','user2','user3']
    valid_passwords = ['pass1','pass2','pass3']
    if username in valid_users and password == valid_passwords[valid_users.index(username)]:
            print(st.success("You have Sign Up Successfully"))
    else:
        print(st.error("Invalid Username or Password"))

st.text_input("Enter Your Name")
st.text_input("Enter Your Paasword")
st.text_input("Renter Your Password")
st.button("Sign in")

st.success("You have Sign Up Successfully")