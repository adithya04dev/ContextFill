import streamlit as st
from agent import main 
# Create two text input fields
input_1 = st.text_input("Enter the form URL.")
input_2 = st.text_input("Enter the user context to be filled.")

# Add a submit button
if st.button("Submit"):
    # Action to take on submit
    
    st.write("You entered:")
    st.write(f"Input 1: {input_1}")
    st.write(f"Input 2: {input_2}")
    main(input_1,input_2)
