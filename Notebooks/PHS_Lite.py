import streamlit as st
import pandas as pd
from streamlit_card import card
from streamlit_modal import Modal
import streamlit.components.v1 as components
from PIL import Image 

st.set_page_config(layout="wide")

with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
    

st.write("""# PHS""")

class HomePage:
    def __init__(self):
        pass
    def welcome_scn(self):
         with st.container():
            # st.write("#### Advanced Level")
            col1, col2,col3 = st.columns([5,5,5],gap='small')
            # st.image("./23.png")
            with col1:
                # st.write('Heath Scores')
                i1=Image.open('./media/welcome/9045622.jpg').resize((350,400))
                st.image(i1)
                st.button("Heath Scores", type="primary")
            with col2:
                # st.write('Exercises')
                i2=Image.open('./media/welcome/4058411.jpg').resize((350,400))
                st.image(i2)
                st.button("Exercises", type="primary")
            with col3:
                # st.write('Yoga Asanass')
                i3=Image.open('./media/welcome/6454159.jpg').resize((350,400))
                st.image(i3)
                st.button("Yoga Asanas", type="primary")
            # with col4:
            #     card(title="Hello World!",text="Some description",image="https://static.streamlit.io/examples/dog.jpg" ,url="https://github.com/gamcoh/st-card",key='b4',styles={ "card": {"width": "200px",  "height": "300px", "border-radius": "60px", "box-shadow": "0 0 10px rgba(0,0,0,0.5)" }, "text": { "font-family": "serif"} })
            # with col5:
            #     card(title="Hello World!",text="Some description",image="https://static.streamlit.io/examples/dog.jpg" ,url="https://github.com/gamcoh/st-card",key='b5',styles={ "card": {"width": "200px",  "height": "300px", "border-radius": "60px", "box-shadow": "0 0 10px rgba(0,0,0,0.5)" }, "text": { "font-family": "serif"} })
        
         with st.container():
            # st.write("#### Advanced Level")
            col1, col2,col3 = st.columns(3)#([5,5,5],gap='small')
            with col1:
                # st.write('Home Remedies')
                i4=Image.open('./media/welcome/6707511.jpg').resize((350,400))
                st.image(i4)
                st.button("Home Remedies", type="primary")
            with col2:
                # st.write('Reduce Stress')
                i5=Image.open('./media/welcome/young-woman-suffering-from-headache.jpg').resize((350,400))
                st.image(i5)
                st.button("Reduce Stress", type="primary")
            with col3:
                # st.write('Health Guidelines')
                i6=Image.open('./media/welcome/7780771.jpg').resize((350,400))
                st.image(i6)
                st.button("Health Guidelines", type="primary")
            # with col4:
            #     card(title="Hello World!",text="Some description",image="https://static.streamlit.io/examples/dog.jpg" ,url="https://github.com/gamcoh/st-card",key='b4',styles={ "card": {"width": "200px",  "height": "300px", "border-radius": "60px", "box-shadow": "0 0 10px rgba(0,0,0,0.5)" }, "text": { "font-family": "serif"} })
            # with col5:
            #     card(title="Hello World!",text="Some description",image="https://static.streamlit.io/examples/dog.jpg" ,url="https://github.com/gamcoh/st-card",key='b5',styles={ "card": {"width": "200px",  "height": "300px", "border-radius": "60px", "box-shadow": "0 0 10px rgba(0,0,0,0.5)" }, "text": { "font-family": "serif"} })


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
            col1, col2, col3, col4, col5 = st.columns([5,5,5,5,5],gap='large')
            with col1:
                st.markdown('<a href="https://example.com/new_page" style="margin: 10px;"><img src="https://static.streamlit.io/examples/cat.jpg" width="150"></a>', unsafe_allow_html=True)
            with col2:
                 st.markdown('<a href="https://example.com/new_page" style="margin: 10px;"><img src="https://static.streamlit.io/examples/dog.jpg" width="150"></a>', unsafe_allow_html=True)
            with col3:
                st.markdown('<a href="https://example.com/new_page" style="margin: 10px;"><img src="https://static.streamlit.io/examples/owl.jpg" width="150"></a>', unsafe_allow_html=True)
            with col4:
                st.markdown('<a href="https://example.com/new_page" style="margin: 10px;"><img src="https://static.streamlit.io/examples/cat.jpg" width="150"></a>', unsafe_allow_html=True)
            with col5:
                st.markdown('<a href="https://example.com/new_page" style="margin: 10px;"><img src="https://static.streamlit.io/examples/cat.jpg" width="150"></a>', unsafe_allow_html=True)
        with st.container():
            st.write("#### Advanced Level")
            col1, col2, col3, col4, col5 = st.columns([5,5,5,5,5],gap='small')
            with col1:
                card(title="Hello World!",text="Some description",image="https://static.streamlit.io/examples/dog.jpg" ,url="https://github.com/gamcoh/st-card",key='b1',styles={ "card": {"width": "200px",  "height": "300px", "border-radius": "60px", "box-shadow": "0 0 10px rgba(0,0,0,0.5)" }, "text": { "font-family": "serif"} })
            with col2:
                card(title="Hello World!",text="Some description",image="https://static.streamlit.io/examples/dog.jpg" ,url="https://github.com/gamcoh/st-card",key='b2',styles={ "card": {"width": "200px",  "height": "300px", "border-radius": "60px", "box-shadow": "0 0 10px rgba(0,0,0,0.5)" }, "text": { "font-family": "serif"} })
            with col3:
                card(title="Hello World!",text="Some description",image="https://static.streamlit.io/examples/dog.jpg" ,url="https://github.com/gamcoh/st-card",key='b3',styles={ "card": {"width": "200px",  "height": "300px", "border-radius": "60px", "box-shadow": "0 0 10px rgba(0,0,0,0.5)" }, "text": { "font-family": "serif"} })
            with col4:
                card(title="Hello World!",text="Some description",image="https://static.streamlit.io/examples/dog.jpg" ,url="https://github.com/gamcoh/st-card",key='b4',styles={ "card": {"width": "200px",  "height": "300px", "border-radius": "60px", "box-shadow": "0 0 10px rgba(0,0,0,0.5)" }, "text": { "font-family": "serif"} })
            with col5:
                card(title="Hello World!",text="Some description",image="https://static.streamlit.io/examples/dog.jpg" ,url="https://github.com/gamcoh/st-card",key='b5',styles={ "card": {"width": "200px",  "height": "300px", "border-radius": "60px", "box-shadow": "0 0 10px rgba(0,0,0,0.5)" }, "text": { "font-family": "serif"} })
        with st.container():
            st.write("This is inside the container3")
        pass
    
    def yoga(self):
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
        pass
            
            
homepage=HomePage()
# homepage.health_check()
# homepage.exercise_rec()
# homepage.yoga()
homepage.welcome_scn()