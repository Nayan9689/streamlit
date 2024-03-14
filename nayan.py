import streamlit as st

st.title("Multi-Select")

# Defining Multi_Select with No Pre-Selection
hobbies = st.multiselect(
    'What are your Hobbies',
    ['Reading', 'Cooking', 'Watching Movies/TV Series', 'Playing', 'Drawing', 'Hiking'])


st.title('Creating Dropdown')

# Creating Dropdown
# hobby = st.selectbox('Choose your hobby: ',
#         ('Books', 'Movies', 'Sports'))


hobby = st.selectbox('Choose your hobby: ',
        ('Books', 'Movies', 'Sports'),
        index=1)
st.title('Pre-Select')

check = st.checkbox('Accept all Terms and Conditions***', value=True)


st.title('Creating Checkboxes')

st.write('Select your Hobies:')

# Defining Checkboxes
check_1 = st.checkbox('Books')
check_2 = st.checkbox('Movies')
check_3 = st.checkbox('Sports')
st.title('Creating Radio Buttons')

# Defining Radio Button with index value
gender = st.radio(
    "Select your Gender",
    ('Male', 'Female', 'Others'),
    index=1)

if gender == 'Male':
    st.write('You have selected Male.')
elif gender == 'Female':
    st.write("You have selected Female.")
else:
    st.write("You have selected Others.")

st.title('Creating Radio Buttons')

# Defining Radio Button
gender = st.radio(
    "Select your Gender",
    ('Male', 'Female', 'Others'))

if gender == 'Male':
    st.write('You have selected Male.')
elif gender == 'Female':
    st.write("You have selected Female.")
else:
    st.write("You have selected Others.")



st.title('Creating a Button')

# Defining Button
button = st.button('Click Here')

if button:
    st.write('You have clicked the Button')
else:
     st.write('You have not clicked the Button')



# Create number input
num = st.number_input("Enter your Number", 0, 10, 5, 2)

st.write("Min. Value is 0,  \n  Max. value is 10")

st.write("Default Value is 5,  \n  Step Size value is 2")

st.write("Total value after adding Number entered with step value is:", num)

import streamlit as st

#Defining Columns
col1, col2 = st.columns(2)

# Inserting Elements in column 1
col1.write("First Column")
col1.image("OIP.jpeg")

# Inserting Elements in column 2
col2.write("Second Column")
col2.image("OIP.jpeg")


from PIL import Image

img = Image.open("OIP.jpeg")

st.title("Spaced Out Coulmns")

# Defining two Rows
for _ in range(2):
    # Defining no. of columns with size
    cols = st.columns((3, 1, 2, 1))
    cols[0].image(img)
    cols[1].image(img)
    cols[2].image(img)
    cols[3].image(img)


img = Image.open("OIP.jpeg")

st.title("Padding")

# Defining Padding with columns
col1, padding, col2 = st.columns((10,2,10))

with col1:
    col1.image(img)

with col2:
    col2.image(img)


st.title('Exapanders')

import numpy as np
# Defining Expanders
with st.expander("Streamlit with Python"):
    st.write("Develop ML Applications in Minutes!!!!")

st.title("Container")

with st.container():
   st.write("Element Inside Contianer")

   # Defining Chart Element
   st.line_chart(np.random.randn(40, 4))

st.write("Element Outside Container")




# Sidebar
st.sidebar.title("Sidebar")
st.sidebar.radio("Are you a New User", ["Yes", "No"])
st.sidebar.slider("Select a Number", 0,10)

st.title("Echo")
with st.echo():
    txt = st.text_input('Text')
    if not txt:
        st.warning('Input a text to see sample code.')
        st.stop()
    st.success('Thank you for text input.')

st.success("Successful")
st.warning("Warning")
st.info("Info")
st.error("Error")
st.exception("It is an exception")
pass