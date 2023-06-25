import streamlit as st
import time
import numpy as np


st.set_page_config(page_title="Past Sleeps", page_icon="🗂️")

st.markdown("# 🗂️ Past Sleeps")
st.sidebar.header("Past Sleeps")
st.write(
    """Take a look at all your great work!"""
)

progress_bar = st.sidebar.progress(0)
status_text = st.sidebar.empty()
last_rows = np.random.randn(1, 1)
chart = st.line_chart(last_rows)

for i in range(1, 20):
    new_rows = last_rows[-1, :] + np.random.randn(5, 1).cumsum(axis=0)
    status_text.text("%i*5%% Complete" % i*5)
    chart.add_rows(new_rows)
    progress_bar.progress(i*5)
    last_rows = new_rows
    time.sleep(0.05)

progress_bar.empty()
