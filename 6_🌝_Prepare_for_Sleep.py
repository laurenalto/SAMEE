import streamlit as st
import time



st.set_page_config(page_title="Prepare for Sleep", page_icon="🌝")

st.markdown("# 🌝 Prepare for Sleep")
st.sidebar.header("🌝 Prepare for Sleep")
st.write(
    """Ready to catch some Z's? Let's get you ready for bed!"""
)

#depending on options selected, ask whether they completed the task
#iterate through the list of tasks using a loop
#preset amount of time for each task
# hard coded example

# set out clothes for tomorrow, change into pyjamas, brush teeth, floss, wash face

def count_down(ts):
    while ts:
        mins, secs = divmod(ts, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        st.write(timer, end="\r")
        time.sleep(1)
        ts -= 1
        
st.write('## 1. Set out clothes for tomorrow 🧥')
clothes = st.button("Start")
if clothes:
    #timer for 2 minutes goes off to set out clothes
    count_down(120)
    

    