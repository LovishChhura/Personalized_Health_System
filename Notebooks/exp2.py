# import requests
# import json
# import pprint
# from datetime import date
# from datetime import timedelta

# # today = date.today() # or you can do today = date.today() for today's date
# today = date(2014, 10, 9)
# weekdate=str(today-timedelta(days=7))

# response=requests.get('https://newsapi.org/v2/top-headlines?country=in&category=health&from={weekdate}&sortBy=publishedAt&apiKey=64f00867b3db40f79eb479d459468b84')

# # mydict=json.loads(response.text)
# # pprint.pprint(mydict)
# mydict=response.json()
# pprint.pprint(mydict)

import streamlit as st

# Create a session state to persist the widget state
if "widget_state" not in st.session_state:
    st.session_state.widget_state = "widget1"

# Widget 1
if st.session_state.widget_state == "widget1":
    widget1_value = st.slider("Slider for Widget 1", 0, 100)
    st.write("Widget 1 value:", widget1_value)

# Widget 2
elif st.session_state.widget_state == "widget2":
    widget2_value = st.text_input("Text Input for Widget 2", "")
    st.write("Widget 2 value:", widget2_value)

# Button to switch between widgets
if st.button("Switch Widget"):
    if st.session_state.widget_state == "widget1":
        st.session_state.widget_state = "widget2"
    else:
        st.session_state.widget_state = "widget1"
