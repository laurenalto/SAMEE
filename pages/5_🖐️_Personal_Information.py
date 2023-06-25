import streamlit as st
import datetime

st.set_page_config(page_title="Personal Information", page_icon="🖐️")

st.markdown("# 😉 {name}'s Personal Information".format(name="Sammy"))
st.sidebar.header("Personal Information")
st.write(
    """Set your personal information to receive customized sleep recommendations and connect with your caregivers."""
)

#date of birth, gender, height, weight, allergies, medications, medical conditions, caregiver contact info

d = st.date_input(
    "Date of Birth",
    datetime.date(2019, 7, 6))

sex = st.radio('Sex', ('Male', 'Female', 'Intersex','Other'))
gender = st.radio('Gender', ('Male', 'Female', 'Non-Binary', 'Transgender','Other'))

allergies = st.text_input('Allergies', '')
height = st.text_input('Height (cm)', '') 
weight = st.text_input('Weight (kg)', '')
medications = st.text_input('Medications', '')
conditions = st.text_input('Medical Conditions', '')

caregiver = st.radio("Do you have a caregiver?", ("Yes", "No"))
if caregiver == "Yes":
    caregiverName = st.text_input('Caregiver Name', '')
    caregiverNum = st.text_input('Caregiver Phone Number', '')
    caregiverEmail = st.text_input('Caregiver Email', '')
    
physician = st.radio("Would your physician like to be added to your profile?", ("Yes", "No"))
if physician == "Yes":
    physicianName = st.text_input('Name', '')
    physicianNum = st.text_input('Phone Number', '')
    physicianEmail = st.text_input('Email', '')
    
    
#save button

