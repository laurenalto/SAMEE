import streamlit as st

from datetime import date
from streamlit_extras.let_it_rain import rain

today = date.today()
d2 = today.strftime("%B %d, %Y")


st.set_page_config(
    page_title="Welcome!",
    page_icon="👋",
)

#don't forget to change for demo
#plan:, 30 min per page, finish by 3, record vid, sleep wake up for final edits, submit by 5
#page 1: sign in page
# page 2: questionnaire/ settings
# page 3 night routine
# page 4 track progress -> rewards
# page 5 connect with medical staff
# page 6 medical recommendations/instructions

# additional resources
user = {"name": "Sammy", "pwd": "a", "userName": "a"}

st.write("# Welcome to Samee! 👋")
#update to 


# depending on the time, say good evening, good morning, good afternoon
# happens after you sign in

#to do: show date and time automatically on main page



st.sidebar.success("Select a routine above.")

st.markdown(
    """
    It's time to sleep!
    Samee (Sleep Assistant Meets Electronic Encouragement) is a virtual sleep assistant designed to help you complete your sleep routines. Please **sign-in** to 
    track your progress and connect with your caregivers.
  
"""
)
#get current time and date

 ### keeping for template 
    # - Use a neural net to [analyze the Udacity Self-driving Car Image
    #     Dataset](https://github.com/streamlit/demo-self-driving)
    # - Explore a [New York City rideshare dataset](https://github.com/streamlit/demo-uber-nyc-pickups)
    
userIn = st.text_input('Username', '')
userPwd = st.text_input('Password', '')

if userIn == user["userName"] and userPwd == user["pwd"]:
    st.success('Welcome {}'.format(user["name"]))
    rain(
    emoji="👋",
    font_size=44,
    falling_speed=8,
    animation_length="5s",
)
    st.write("It's ", d2, "!")
    st.write("It's time to sleep! Check the tabs to complete your nightly routines.")
    # other pages now become available
else:
    st.warning("Incorrect Username or Password. Please try again.")
    

    
    
    
    