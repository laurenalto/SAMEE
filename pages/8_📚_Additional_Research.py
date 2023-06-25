import streamlit as st
from datetime import date
from streamlit_extras.let_it_rain import rain


st.set_page_config(
    page_title="Additional Sources",
    page_icon="📚",
)

st.write("# Additional Sources")

st.markdown(
    """
    Take a look at the **personlized** resources below to improve your sleep! Make sure to review those provided by your **caregivers and physicians**.
    
    **Personalized Recommendations**
    - Sleeping for Alzheimers [- Alzheimers Association](https://www.alz.org/alzheimers-dementia/treatments/for-sleep-changes#:~:text=Sleep%20changes%20in%20Alzheimer%27s%20may,and%20non%2Ddreaming%20sleep%20stages.)
    - Resting to Recharge [National Sleep Foundation](https://www.thensf.org)
    
    **Prescribed Readings**
    - Sleeping for long-term health [- National Institute of Health](https://www.nhlbi.nih.gov/health-topics/sleep-deprivation-and-deficiency)
    - Sleeping for circadian rhythm [- National Institute of Health](https://www.nigms.nih.gov/education/fact-sheets/Pages/circadian-rhythms.aspx)
    - Effects of sleep deprivation [- National Institute of Health](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2656292/)
    
    
"""
)
st.write('Have you finished all the readings? If so, click the button below to request some more, and inform your care provider!')
request = st.button("More Resources!")

if request:
    st.success("Your request has been sent to your care provider!")
    rain(
    emoji="📚",
    font_size=44,
    falling_speed=8,
    animation_length="3s",
    )
    
    
    
    