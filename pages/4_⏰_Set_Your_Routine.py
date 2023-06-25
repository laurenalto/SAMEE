import streamlit as st
import datetime

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
st.write('🛌 Bedtime', bed)
progress_bar.progress(10)

wake = st.time_input('What time would you like to wake up?', datetime.time(6, 45))
st.write('⏰ Alarm', wake)
progress_bar.progress(20)

#calculates sleep time base on bed and wake up time, without day writing
sleepTime = (datetime.datetime.combine(datetime.date.min, wake) - datetime.datetime.combine(datetime.date.min, bed)) + datetime.timedelta(hours=24)
st.write('## You will sleep', sleepTime, 'hours.')

#different messages according to amount of sleep
if sleepTime < datetime.timedelta(hours=6):
    st.write('According to the National Sleep Institute, your desired sleep time is not sustainable. **Please consider going to bed earlier or speaking with your healthcare provider.**')
    #add contact now button
    progress_bar.progress(30)
    
elif sleepTime > datetime.timedelta(hours=8):
    st.write('According to the National Sleep Institute, you are receiving an appropriate amount of sleep time. **Great work!**')
    progress_bar.progress(30)
    
else:
    st.write('According to the National Sleep Institute, you would benefit from another hour of sleep. **Please consider going to bed earlier.**')
    

#check box would you like to receive bedtime reminders?
bedremind = st.radio(
    "Would you like to receive bedtime reminders?",
    ('Yes', 'No'))

if bedremind == 'Yes':
    st.write('Reminder set for', bed)
    progress_bar.progress(50)
    
#ask user if they have a night routine
nr = st.radio(
    "Would you like to create a night routine?",
    ('Yes', 'No'))

if nr == 'Yes':
    st.write('Great! Please select the activities you would like to include in your night routine:')
    options = st.multiselect(
    'Night Routine Activities:',
    ['Brush Teeth', 'Floss', 'Wash Face', 'Change into pyjamas', 'Read', 'Medidate', "Write down tomorrow's goals", 'Stretch', 'Drink water', 'Set alarm', 'Set out clothes for tomorrow', 'Set out breakfast for tomorrow', 'Set out lunch for tomorrow', 'Set out snacks for tomorrow', 'Set out bag for tomorrow', 'Set out keys for tomorrow', 'Set out wallet for tomorrow', 'Set out phone charger for tomorrow', 'Set out work materials for tomorrow', 'Set out gym bag for tomorrow', 'Set out yoga mat for tomorrow', 'Set out running shoes for tomorrow', 'Set out water bottle for tomorrow', 'Set out headphones for tomorrow', 'Set out mask for tomorrow', 'Set out hand sanitizer for tomorrow', 'Set out umbrella for tomorrow'], default=None)
    st.write('You selected:', options)
    progress_bar.progress(80)

    #make table where person can add activities and alot amount of time
    # select from a list, or create new activities
    
saved = st.button("Save Routine")
if saved:
    st.write('Your routine has been saved.')
    progress_bar.progress(100)

    

progress_bar.empty()

# # Streamlit widgets automatically run the script from top to bottom. Since
# # this button is not connected to any other logic, it just causes a plain
# # rerun.
# st.button("Re-run")