import streamlit as st
import datetime
import numpy as np

st.set_page_config(page_title="Set Your Routine", page_icon="⏰")

st.markdown("# Set Your Routine")
st.sidebar.header("Set Your Routine")
st.write(
    """Complete the following questions to set your sleep routine. If you require assistance, please consult with your medical care provider to build the routine accordingly."""
)

progress_bar = st.sidebar.progress(0)
status_text = st.sidebar.empty()

#setting sleep time
bed = st.time_input('What time would you like to go to bed?', datetime.time(20, 30))
st.write('Bedtime reminder is set for', bed)
progress_bar.progress(10)

wake = st.time_input('What time would you like to wake up?', datetime.time(6, 45))
st.write('Alarm is set for', wake)
progress_bar.progress(20)

#calculates sleep time base on bed and wake up time, without day writing
sleepTime = (datetime.datetime.combine(datetime.date.min, wake) - datetime.datetime.combine(datetime.date.min, bed)) + datetime.timedelta(hours=24)
st.write('You will get', sleepTime, 'of sleep.')

#different messages according to amount of sleep
if sleepTime < datetime.timedelta(hours=6):
    st.write('According to the National Sleep Institute, your desired sleep time is not sustainable. **Please consider going to bed earlier or speaking with your healthcare provider.**')
    #add contact now button
    progress_bar.progress(30)
    
elif sleepTime > datetime.timedelta(hours=8):
    st.write('According to the National Sleep Institute, you are have set a legitimate sleep time. **Great work!**')
    progress_bar.progress(30)
    
else:
    st.write('According to the National Sleep Institute, you would benefit from another hour of sleep. **Please consider going to bed earlier.**')
    

#check box would you like to receive bedtime reminders?
st.write('Would you like to receive bedtime reminders?')
st.checkbox('Yes')
st.checkbox('No')

if st.checkbox('Yes'):
    st.write('Reminder set for', bed)
    progress_bar.progress(40)
    
#ask user if they have a night routine
st.write('Would you like to create a night routine?') #add link to night routine page
st.checkbox('Yes')
st.checkbox('No')
if st.checkbox('Yes'):
    st.write('Great! Please select the activities you would like to include in your night routine:')
    
    #make table where person can add activities and alot amount of time
    # select from a list, or create new activities
    st.checkbox('Brush teeth')
    st.checkbox('Floss')
    st.
    progress_bar.progress(50)
    st

# progress_bar.empty()

# # Streamlit widgets automatically run the script from top to bottom. Since
# # this button is not connected to any other logic, it just causes a plain
# # rerun.
# st.button("Re-run")