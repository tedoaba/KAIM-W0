import streamlit as st

# Set page configuration
st.set_page_config(page_title="Streamlit Basics",
                   page_icon=":bar_chart:",
                   layout="wide"
                   )

# Set page title
st.title("Streamlit Basics Tutorial")

# ### Text Input

# Create a text input field
text_input = st.text_input("Enter your name", placeholder="Your Name")

# Display the input text
st.write("Hello, " + text_input + "!")

### Slider

# Create a slider
val = st.slider("Select a value", 0, 10, 0, step=1)

# Display the slider value
st.write("Slider value:", val)

### Button

# Create a button
btn1 = st.button("Click Me")

# Handle button click
if btn1:
    st.write("I got clicked  \U0001f604 ")

### Radio Buttons

# Create radio buttons
radio_val = st.radio("Select an option", ["Option 1", "Option 2", "Option 3"])

# Display the selected option
st.write("Selected option:", radio_val)

### Checkboxes

# Create checkboxes
checkbox_val = st.checkbox("Check me")

# Handle checkbox state
if checkbox_val:
    st.write("Checkbox is checked")
else:
    st.write("Checkbox is not checked")

### Selectbox

# Create a selectbox
selectbox_val = st.selectbox("Select a color", ["Red", "Green", "Blue"])

# Display the selected color
st.write("Selected color:", selectbox_val)

### Multiselect

# Create a multiselect
multiselect_val = st.multiselect("Select colors", ["Red", "Green", "Blue"])

# Display the selected colors
st.write("Selected colors:", multiselect_val)

### Date and Time

# Create a date input
date_input = st.date_input("Select a date")

# Display the selected date
st.write("Selected date:", date_input)

# Create a time input
time_input = st.time_input("Select a time")

# Display the selected time
st.write("Selected time:", time_input)