import streamlit as st
import pandas as pd
from streamlit_card import card
from streamlit_modal import Modal

import streamlit.components.v1 as components
 
st.write("""# PHS""")

class Home:
    def __init__(self):
        pass
    def health_check(self):
        with st.form("my_form"):
            st.write("Check Your Health Score")
            tempF=st.text_input("Body Temperature:")
            pulse=st.text_input("Body Pulse:")
            respr=st.text_input("Respiration Rate:")
            bpsys=st.text_input("Bystolic BP:")
            bpdia=st.text_input("Diastolic BP:")
            popct=st.text_input("Blood Oxygen:")
            # Every form must have a submit button.
            submitted = st.form_submit_button("Submit")
            if submitted:
                st.write("Submitted")
                healthFrame=pd.DataFrame([[tempF, pulse, respr, bpsys, bpdia, popct]],columns=['tempF','pulse','respr','bpsys','bpdia','popct'])
                st.write(1)
            st.write("Live Happy ")
            
    def exercise_rec(self):
        st.write("### Exercises for you")
        with st.container():
            st.write("#### Beginner Level")
            col1, col2, col3, col4, col5 = st.columns(5)
            with col1:
                # st.header("A cat")
                # st.image("https://static.streamlit.io/examples/cat.jpg")
                card(title="Hello World!", text="", image="http://placekitten.com/200/300", url="https://github.com/gamcoh/st-card")
            with col2:
                st.header("A dog")
                st.image("https://static.streamlit.io/examples/dog.jpg")
            with col3:
                st.header("An owl")
                st.image("https://static.streamlit.io/examples/owl.jpg")
            with col4:
                st.header("A cat")
                st.image("https://static.streamlit.io/examples/cat.jpg")
            with col5:
                st.header("A cat")
                st.image("https://static.streamlit.io/examples/cat.jpg")
        with st.container():
            st.write("#### Advanced Level")
            col1, col2, col3, col4, col5 = st.columns(5)
            with col1:
                st.header("A cat")
                st.image("https://static.streamlit.io/examples/cat.jpg")
            with col2:
                st.header("A dog")
                st.image("https://static.streamlit.io/examples/dog.jpg")
            with col3:
                st.header("An owl")
                st.image("https://static.streamlit.io/examples/owl.jpg")
            with col4:
                st.header("A cat")
                st.image("https://static.streamlit.io/examples/cat.jpg")
            with col5:
                st.header("A cat")
                st.image("https://static.streamlit.io/examples/cat.jpg")
        with st.container():
            st.write("This is inside the container3")
        pass
            
            
homepage=Home()
# homepage.health_check()
homepage.exercise_rec()