import streamlit as st
import pandas as pd
from streamlit_card import card
from streamlit_modal import Modal
import streamlit.components.v1 as components
from PIL import Image 
import base64
from pathlib import Path
from streamlit_option_menu import option_menu
from streamlit_carousel import carousel
import glob

st.set_page_config(layout="wide")

st.markdown('<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN" crossorigin="anonymous">', unsafe_allow_html=True)



    

# st.write("""# PHS""")

class HomePage:
    def __init__(self):
        pass
    def welcome_scn(self):
        with open('style.css') as f:
            st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
        selected=option_menu(
            menu_title=None, 
            options=["Home","Heath Score","Exercises","Yoga Asanas","Home Remedies","Reduce Stress","Health Guidelines"],
            icons=("house","coin","controller","emoji-heart-eyes","apple","balloon-heart","hospital"),
            menu_icon="cast",
            default_index=0,
            orientation="horizontal",
        )
        if selected=="Home":
            pass
        
        st.title('PHS')
        
        # logo=Image.open('./AmmiM.png').resize((200,200))
        # st.image(logo)
        
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
        def modal_dis():
            modal = Modal("hi",key="Demo")
            with modal.container():
                                    # st.write("Text goes here")
                                    html_string = '''<h1>HTML string in RED</h1><script language="javascript">document.querySelector("h1").style.color = "red";</script>'''
                                    components.html(html_string)
                                    # st.write("Some fancy text")
                                    # value = st.checkbox("Check me")
                                    # st.write(f"Checkbox checked: {value}")
            
        selected=option_menu(
            menu_title=None, 
            options=["Home","Heath Score","Excercises","Yoga Asanas","Home Remedies","Reduce Stress","Health Guidelines"],
            icons=("house","coin","controller","emoji-heart-eyes","apple","balloon-heart","hospital"),
            menu_icon="cast",
            default_index=1,
            orientation="horizontal",
        )
        if selected=="Home":
            pass
        
        st.title('PHS')
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
                if tempF and pulse and respr and bpsys and bpdia and popct:
                    healthFrame=pd.DataFrame([[tempF, pulse, respr, bpsys, bpdia, popct]],columns=['tempF','pulse','respr','bpsys','bpdia','popct'])
                    st.write('''<h3>Your health score is <b>1</b></h3>''',unsafe_allow_html=True)                                   
                    st.write('''<h5 style="color:green"><i>Health status: Healthy</i><h5>''',unsafe_allow_html=True)                                   
                else:
                    # st.warning('Fill all fields', icon="⚠️")
                    st.error('Fill all fields', icon="🚨")
                # st.write("Submitted")
                
                # st.write(tempF)
                # print(type(tempF))
            st.write("Live Happy ")
    
    def exercise_scn(self):
        with open('style.css') as f:
            st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
        selected=option_menu(
            menu_title=None, 
            options=["Home","Heath Score","Excercises","Yoga Asanas","Home Remedies","Reduce Stress","Health Guidelines"],
            icons=("house","coin","controller","emoji-heart-eyes","apple","balloon-heart","hospital"),
            menu_icon="cast",
            default_index=2,
            orientation="horizontal",
        )
        if selected=="Home":
            pass
        
        st.title('PHS')
        
        # logo=Image.open('./AmmiM.png').resize((200,200))
        # st.image(logo)
        
        with st.container():
            # st.write("#### Advanced Level")
            col1, col2,col3 = st.columns([5,5,5],gap='small')
            # st.image("./23.png")
            with col1:
                # st.write('Heath Scores')
                i1=Image.open('./media/welcome/chest.jpg').resize((350,400))
                st.image(i1)
                st.button("Chest", type="primary")
            with col2:
                # st.write('Exercises')
                i2=Image.open('./media/welcome/biceps.jpg').resize((350,400))
                st.image(i2)
                st.button("Biceps", type="primary")
            with col3:
                # st.write('Yoga Asanass')
                i3=Image.open('./media/welcome/triceps.jpg').resize((350,400))
                st.image(i3)
                st.button("Triceps", type="primary")
            # with col4:
            #     card(title="Hello World!",text="Some description",image="https://static.streamlit.io/examples/dog.jpg" ,url="https://github.com/gamcoh/st-card",key='b4',styles={ "card": {"width": "200px",  "height": "300px", "border-radius": "60px", "box-shadow": "0 0 10px rgba(0,0,0,0.5)" }, "text": { "font-family": "serif"} })
            # with col5:
            #     card(title="Hello World!",text="Some description",image="https://static.streamlit.io/examples/dog.jpg" ,url="https://github.com/gamcoh/st-card",key='b5',styles={ "card": {"width": "200px",  "height": "300px", "border-radius": "60px", "box-shadow": "0 0 10px rgba(0,0,0,0.5)" }, "text": { "font-family": "serif"} })
        
        with st.container():
            # st.write("#### Advanced Level")
            col1, col2,col3 = st.columns(3)#([5,5,5],gap='small')
            with col1:
                # st.write('Home Remedies')
                i4=Image.open('./media/welcome/shoulder.jpg').resize((350,400))
                st.image(i4)
                st.button("Shoulders", type="primary")
            with col2:
                # st.write('Reduce Stress')
                i5=Image.open('./media/welcome/back.jpg').resize((350,400))
                st.image(i5)
                st.button("Back", type="primary")
            with col3:
                # st.write('Health Guidelines')
                i6=Image.open('./media/welcome/leg.jpg').resize((350,400))
                st.image(i6)
                st.button("Leg", type="primary")        
    def exercise_rec(self):
        with open('style2.css') as f:
            st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
        
        def img_to_bytes(img_path):
            img_bytes = Path(img_path).read_bytes()
            encoded = base64.b64encode(img_bytes).decode()
            return encoded
        def img_to_html(img_path):
            img_html = "<img src='data:image/png;base64,{}' class='img-fluid'>".format(img_to_bytes(img_path))
            return img_html

        selected=option_menu(
            menu_title=None, 
            options=["Home","Heath Score","Exercises","Yoga Asanas","Home Remedies","Reduce Stress","Health Guidelines"],
            icons=("house","coin","controller","emoji-heart-eyes","apple","balloon-heart","hospital"),
            menu_icon="cast",
            default_index=2,
            orientation="horizontal",
        )
        if selected=="Home":
            pass
        tab1, tab2 = st.tabs(["Beginners", "Advanced"])
        with tab1:
            # st.header("A cat")
            # st.image("https://static.streamlit.io/examples/cat.jpg", width=200)
            with st.container():
                st.write("#### Beginners Level")
                col1, col2, col3, col4, col5 = st.columns([5,5,5,5,5],gap='small')
                with col1:
                    with col1:
                        i1=Image.open('./media/welcome/chest.jpg').resize((270,300))
                        col1.image(i1)
                        col1.button("b1a", type="primary")
                    with col2:
                        # st.write('Exercises')
                        i2=Image.open('./media/welcome/biceps.jpg').resize((270,300))
                        col2.image(i2)
                        col2.button("b2a", type="primary")
                    with col3:
                        # st.write('Yoga Asanass')
                        i3=Image.open('./media/welcome/triceps.jpg').resize((270,300))
                        col3.image(i3)
                        col3.button("b3a", type="primary")
                    with col4:
                        # st.write('Yoga Asanass')
                        i3=Image.open('./media/welcome/triceps.jpg').resize((270,300))
                        col4.image(i3)
                        col4.button("b4a", type="primary")
                    with col4:
                        # st.write('Yoga Asanass')
                        i3=Image.open('./media/welcome/triceps.jpg').resize((270,300))
                        col5.image(i3)
                        col5.button("b5a", type="primary")
        with tab2:
            with st.container():
                st.write("#### Advanced Level")
                col1, col2, col3, col4, col5 = st.columns([5,5,5,5,5],gap='small')
                with col1:
                    with col1:
                        i1=Image.open('./media/welcome/chest.jpg').resize((270,300))
                        col1.image(i1)
                        col1.button("a1a", type="primary")
                    with col2:
                        # st.write('Exercises')
                        i2=Image.open('./media/welcome/biceps.jpg').resize((270,300))
                        col2.image(i2)
                        col2.button("a2a", type="primary")
                    with col3:
                        # st.write('Yoga Asanass')
                        i3=Image.open('./media/welcome/triceps.jpg').resize((270,300))
                        col3.image(i3)
                        col3.button("a3a", type="primary")
                    with col4:
                        # st.write('Yoga Asanass')
                        i3=Image.open('./media/welcome/triceps.jpg').resize((270,300))
                        col4.image(i3)
                        col4.button("a4a", type="primary")
                    with col4:
                        # st.write('Yoga Asanass')
                        i3=Image.open('./media/welcome/triceps.jpg').resize((270,300))
                        col5.image(i3)
                        col5.button("a5a", type="primary")
        
        # st.write("### Exercises for you")
        # with st.container():
        #     st.write("#### Beginner Level")
        #     col1, col2, col3, col4, col5 = st.columns([5,5,5,5,5],gap='large')
        #     with col1:
        #         st.markdown('<a href="https://example.com/new_page" style="margin: 10px;"><img src="https://static.streamlit.io/examples/cat.jpg" width="150"></a>', unsafe_allow_html=True)
        #     with col2:
        #          st.markdown('<a href="https://example.com/new_page" style="margin: 10px;"><img src="https://static.streamlit.io/examples/dog.jpg" width="150"></a>', unsafe_allow_html=True)
        #     with col3:
        #         st.markdown('<a href="https://example.com/new_page" style="margin: 10px;"><img src="https://static.streamlit.io/examples/owl.jpg" width="150"></a>', unsafe_allow_html=True)
        #     with col4:
        #         st.markdown('<a href="https://example.com/new_page" style="margin: 10px;"><img src="https://static.streamlit.io/examples/cat.jpg" width="150"></a>', unsafe_allow_html=True)
        #     with col5:
        #         st.markdown('<a href="https://example.com/new_page" style="margin: 10px;"><img src="https://static.streamlit.io/examples/cat.jpg" width="150"></a>', unsafe_allow_html=True)
        # with st.container():
        #     st.write("#### Advanced Level")
        #     col1, col2, col3, col4, col5 = st.columns([5,5,5,5,5],gap='small')
        #     with col1:
        #         card(title="Hello World!",text="Some description",image="https://static.streamlit.io/examples/dog.jpg" ,url="https://github.com/gamcoh/st-card",key='b1',styles={ "card": {"width": "200px",  "height": "300px", "border-radius": "60px", "box-shadow": "0 0 10px rgba(0,0,0,0.5)" }, "text": { "font-family": "serif"} })
        #     with col2:
        #         card(title="Hello World!",text="Some description",image="https://static.streamlit.io/examples/dog.jpg" ,url="https://github.com/gamcoh/st-card",key='b2',styles={ "card": {"width": "200px",  "height": "300px", "border-radius": "60px", "box-shadow": "0 0 10px rgba(0,0,0,0.5)" }, "text": { "font-family": "serif"} })
        #     with col3:
        #         card(title="Hello World!",text="Some description",image="https://static.streamlit.io/examples/dog.jpg" ,url="https://github.com/gamcoh/st-card",key='b3',styles={ "card": {"width": "200px",  "height": "300px", "border-radius": "60px", "box-shadow": "0 0 10px rgba(0,0,0,0.5)" }, "text": { "font-family": "serif"} })
        #     with col4:
        #         card(title="Hello World!",text="Some description",image="https://static.streamlit.io/examples/dog.jpg" ,url="https://github.com/gamcoh/st-card",key='b4',styles={ "card": {"width": "200px",  "height": "300px", "border-radius": "60px", "box-shadow": "0 0 10px rgba(0,0,0,0.5)" }, "text": { "font-family": "serif"} })
        #     with col5:
        #         card(title="Hello World!",text="Some description",image="https://static.streamlit.io/examples/dog.jpg" ,url="https://github.com/gamcoh/st-card",key='b5',styles={ "card": {"width": "200px",  "height": "300px", "border-radius": "60px", "box-shadow": "0 0 10px rgba(0,0,0,0.5)" }, "text": { "font-family": "serif"} })
        # with st.container():
        #     st.write("This is inside the container3")
        pass
    def yoga_scn(self):
        with open('style.css') as f:
            st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
        selected=option_menu(
            menu_title=None, 
            options=["Home","Heath Score","Excercises","Yoga Asanas","Home Remedies","Reduce Stress","Health Guidelines"],
            icons=("house","coin","controller","emoji-heart-eyes","apple","balloon-heart","hospital"),
            menu_icon="cast",
            default_index=3,
            orientation="horizontal",
        )
        if selected=="Home":
            pass
        
        st.title('PHS Yoga Asanas')
        
        # logo=Image.open('./AmmiM.png').resize((200,200))
        # st.image(logo)
        
        with st.container():
            # st.write("#### Advanced Level")
            col1, col2,col3 = st.columns([5,5,5],gap='small')
            # st.image("./23.png")
            with col1:
                # st.write('Heath Scores')
                i1=Image.open('./media/welcome/standing pose.jpg').resize((350,400))
                st.image(i1)
                st.button("Standing Asanas", type="primary")
            with col2:
                # st.write('Exercises')
                i2=Image.open('./media/welcome/sitting pose.jpg').resize((350,400))
                st.image(i2)
                st.button("Sitting Asanas", type="primary")
            with col3:
                # st.write('Yoga Asanass')
                i3=Image.open('./media/welcome/laying on back pose.jpg').resize((350,400))
                st.image(i3)
                st.button("Laying on Back Asanas", type="primary")
            # with col4:
            #     card(title="Hello World!",text="Some description",image="https://static.streamlit.io/examples/dog.jpg" ,url="https://github.com/gamcoh/st-card",key='b4',styles={ "card": {"width": "200px",  "height": "300px", "border-radius": "60px", "box-shadow": "0 0 10px rgba(0,0,0,0.5)" }, "text": { "font-family": "serif"} })
            # with col5:
            #     card(title="Hello World!",text="Some description",image="https://static.streamlit.io/examples/dog.jpg" ,url="https://github.com/gamcoh/st-card",key='b5',styles={ "card": {"width": "200px",  "height": "300px", "border-radius": "60px", "box-shadow": "0 0 10px rgba(0,0,0,0.5)" }, "text": { "font-family": "serif"} })
        
        with st.container():
            # st.write("#### Advanced Level")
            col1, col2,col3 = st.columns(3)#([5,5,5],gap='small')
            with col1:
                # st.write('Home Remedies')
                i4=Image.open('./media/welcome/laying on stomach pose.jpg').resize((350,400))
                st.image(i4)
                st.button("Laying on Stomach Asanas", type="primary")
            with col2:
                # st.write('Reduce Stress')
                i5=Image.open('./media/welcome/balancing pose.jpg').resize((350,400))
                st.image(i5)
                st.button("Balancing Asanas", type="primary")
            with col3:
                # st.write('Health Guidelines')
                i6=Image.open('./media/welcome/eyes pose.jpg').resize((350,400))
                st.image(i6)
                st.button("Eyes Asanas", type="primary") 
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
    
    def yoga_rec(self):
        with open('style2.css') as f:
            st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
        
        def img_to_bytes(img_path):
            img_bytes = Path(img_path).read_bytes()
            encoded = base64.b64encode(img_bytes).decode()
            return encoded
        def img_to_html(img_path):
            img_html = "<img src='data:image/png;base64,{}' class='img-fluid'>".format(img_to_bytes(img_path))
            return img_html

        selected=option_menu(
            menu_title=None, 
            options=["Home","Heath Score","Exercises","Yoga Asanas","Home Remedies","Reduce Stress","Health Guidelines"],
            icons=("house","coin","controller","emoji-heart-eyes","apple","balloon-heart","hospital"),
            menu_icon="cast",
            default_index=3,
            orientation="horizontal",
        )
        if selected=="Home":
            pass
        tab1, tab2, tab3 = st.tabs(["Beginners","Intermediate", "Advanced"])
        with tab1:
            # st.header("A cat")
            # st.image("https://static.streamlit.io/examples/cat.jpg", width=200)
            with st.container():
                st.write("#### Beginners Level")
                col1, col2, col3, col4, col5 = st.columns([5,5,5,5,5],gap='small')
                with col1:
                    with col1:
                        i1=Image.open('./media/welcome/chest.jpg').resize((270,300))
                        col1.image(i1)
                        col1.button("b1a", type="primary")
                    with col2:
                        # st.write('Exercises')
                        i2=Image.open('./media/welcome/biceps.jpg').resize((270,300))
                        col2.image(i2)
                        col2.button("b2a", type="primary")
                    with col3:
                        # st.write('Yoga Asanass')
                        i3=Image.open('./media/welcome/triceps.jpg').resize((270,300))
                        col3.image(i3)
                        col3.button("b3a", type="primary")
                    with col4:
                        # st.write('Yoga Asanass')
                        i3=Image.open('./media/welcome/triceps.jpg').resize((270,300))
                        col4.image(i3)
                        col4.button("b4a", type="primary")
                    with col4:
                        # st.write('Yoga Asanass')
                        i3=Image.open('./media/welcome/triceps.jpg').resize((270,300))
                        col5.image(i3)
                        col5.button("b5a", type="primary")
        with tab2:
            with st.container():
                st.write("#### Intermediate Level")
                col1, col2, col3, col4, col5 = st.columns([5,5,5,5,5],gap='small')
                with col1:
                    with col1:
                        i1=Image.open('./media/welcome/chest.jpg').resize((270,300))
                        col1.image(i1)
                        col1.button("i1a", type="primary")
                    with col2:
                        # st.write('Exercises')
                        i2=Image.open('./media/welcome/biceps.jpg').resize((270,300))
                        col2.image(i2)
                        col2.button("i2a", type="primary")
                    with col3:
                        # st.write('Yoga Asanass')
                        i3=Image.open('./media/welcome/triceps.jpg').resize((270,300))
                        col3.image(i3)
                        col3.button("i3a", type="primary")
                    with col4:
                        # st.write('Yoga Asanass')
                        i3=Image.open('./media/welcome/triceps.jpg').resize((270,300))
                        col4.image(i3)
                        col4.button("i4a", type="primary")
                    with col4:
                        # st.write('Yoga Asanass')
                        i3=Image.open('./media/welcome/triceps.jpg').resize((270,300))
                        col5.image(i3)
                        col5.button("i5a", type="primary")
        with tab3:
            with st.container():
                st.write("#### Advanced Level")
                col1, col2, col3, col4, col5 = st.columns([5,5,5,5,5],gap='small')
                with col1:
                    with col1:
                        i1=Image.open('./media/welcome/chest.jpg').resize((270,300))
                        col1.image(i1)
                        col1.button("a1a", type="primary")
                    with col2:
                        # st.write('Exercises')
                        i2=Image.open('./media/welcome/biceps.jpg').resize((270,300))
                        col2.image(i2)
                        col2.button("a2a", type="primary")
                    with col3:
                        # st.write('Yoga Asanass')
                        i3=Image.open('./media/welcome/triceps.jpg').resize((270,300))
                        col3.image(i3)
                        col3.button("a3a", type="primary")
                    with col4:
                        # st.write('Yoga Asanass')
                        i3=Image.open('./media/welcome/triceps.jpg').resize((270,300))
                        col4.image(i3)
                        col4.button("a4a", type="primary")
                    with col4:
                        # st.write('Yoga Asanass')
                        i3=Image.open('./media/welcome/triceps.jpg').resize((270,300))
                        col5.image(i3)
                        col5.button("a5a", type="primary")        
            
    def homeremedies_scn(self):
        with open('style.css') as f:
            st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
        selected=option_menu(
            menu_title=None, 
            options=["Home","Heath Score","Excercises","Yoga Asanas","Home Remedies","Reduce Stress","Health Guidelines"],
            icons=("house","coin","controller","emoji-heart-eyes","apple","balloon-heart","hospital"),
            menu_icon="cast",
            default_index=4,
            orientation="horizontal",
        )
        if selected=="Home":
            pass
        
        st.title('PHS Home Remedies')
        
        # logo=Image.open('./AmmiM.png').resize((200,200))
        # st.image(logo)
        
        with st.container():
            # st.write("#### Advanced Level")
            col1, col2,col3, col4,col5 = st.columns([5,5,5,5,5],gap='small')
            # st.image("./23.png")
            with col1:
                # st.write('Heath Scores')
                i1=Image.open('./media/welcome/chest.jpg').resize((150,200))
                st.image(i1)
                st.button("Chest", type="primary")
            with col2:
                # st.write('Exercises')
                i2=Image.open('./media/welcome/biceps.jpg').resize((150,200))
                st.image(i2)
                st.button("Biceps", type="primary")
            with col3:
                # st.write('Yoga Asanass')
                i3=Image.open('./media/welcome/triceps.jpg').resize((150,200))
                st.image(i3)
                st.button("Triceps", type="primary")
            with col4:
                # st.write('Yoga Asanass')
                i3=Image.open('./media/welcome/triceps.jpg').resize((150,200))
                st.image(i3)
                st.button("hr4", type="primary")
            with col5:
                # st.write('Yoga Asanass')
                i3=Image.open('./media/welcome/triceps.jpg').resize((150,200))
                st.image(i3)
                st.button("hr5", type="primary")
            
        
        with st.container():
            # st.write("#### Advanced Level")
            col1, col2,col3,col4,col5 = st.columns(5)#([5,5,5],gap='small')
            with col1:
                # st.write('Home Remedies')
                i4=Image.open('./media/welcome/shoulder.jpg').resize((150,200))
                st.image(i4)
                st.button("Shoulders", type="primary")
            with col2:
                # st.write('Reduce Stress')
                i5=Image.open('./media/welcome/back.jpg').resize((150,200))
                st.image(i5)
                st.button("Back", type="primary")
            with col3:
                # st.write('Health Guidelines')
                i6=Image.open('./media/welcome/leg.jpg').resize((150,200))
                st.image(i6)
                st.button("Leg", type="primary")
            with col4:
                # st.write('Health Guidelines')
                i6=Image.open('./media/welcome/leg.jpg').resize((150,200))
                st.image(i6)
                st.button("hr9", type="primary")
            with col5:
                # st.write('Health Guidelines')
                i6=Image.open('./media/welcome/leg.jpg').resize((150,200))
                st.image(i6)
                st.button("hr10", type="primary")
                
    def homeremedies_rec(self):
        with open('style2.css') as f:
            st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
        selected=option_menu(
            menu_title=None, 
            options=["Home","Heath Score","Excercises","Yoga Asanas","Home Remedies","Reduce Stress","Health Guidelines"],
            icons=("house","coin","controller","emoji-heart-eyes","apple","balloon-heart","hospital"),
            menu_icon="cast",
            default_index=4,
            orientation="horizontal",
        )
        if selected=="Home":
            pass
        
        st.title('PHS Home Remedies')
        with st.container():
            st.write("#### Common Cold")
            col1, col2 = st.columns([2,8],gap='small')
            with col1:
                i1=Image.open('./media/welcome/chest.jpg').resize((270,300))
                col1.image(i1)
                
            with col2:
                st.markdown('''<h5>1. Ginger</h5>''',unsafe_allow_html=True)
                st.markdown('''<p>Ginger has antioxidant, antimicrobial, and anti-inflammatory properties. Uses includeTrusted Source reducing muscle pain and managing nausea.Make tea by simmering a few slices of raw ginger root in boiling water.As well as providing hydration, it may soothe muscle pain, ease a sore throat, and reduce nausea, if present.</p><hr/>''',unsafe_allow_html=True)
                st.markdown('''<h5>2. Ginger</h5>''',unsafe_allow_html=True)
                st.markdown('''<p>Ginger has antioxidant, antimicrobial, and anti-inflammatory properties. Uses includeTrusted Source reducing muscle pain and managing nausea.Make tea by simmering a few slices of raw ginger root in boiling water.As well as providing hydration, it may soothe muscle pain, ease a sore throat, and reduce nausea, if present.</p><hr/>''',unsafe_allow_html=True)
                st.markdown('''<h5>3. Ginger</h5>''',unsafe_allow_html=True)
                st.markdown('''<p>Ginger has antioxidant, antimicrobial, and anti-inflammatory properties. Uses includeTrusted Source reducing muscle pain and managing nausea.Make tea by simmering a few slices of raw ginger root in boiling water.As well as providing hydration, it may soothe muscle pain, ease a sore throat, and reduce nausea, if present.</p><hr/>''',unsafe_allow_html=True)
                st.markdown('''<h5>4. Ginger</h5>''',unsafe_allow_html=True)
                st.markdown('''<p>Ginger has antioxidant, antimicrobial, and anti-inflammatory properties. Uses includeTrusted Source reducing muscle pain and managing nausea.Make tea by simmering a few slices of raw ginger root in boiling water.As well as providing hydration, it may soothe muscle pain, ease a sore throat, and reduce nausea, if present.</p><hr/>''',unsafe_allow_html=True)
                st.markdown('''<h5>5. Ginger</h5>''',unsafe_allow_html=True)
                st.markdown('''<p>Ginger has antioxidant, antimicrobial, and anti-inflammatory properties. Uses includeTrusted Source reducing muscle pain and managing nausea.Make tea by simmering a few slices of raw ginger root in boiling water.As well as providing hydration, it may soothe muscle pain, ease a sore throat, and reduce nausea, if present.</p>''',unsafe_allow_html=True)
      
    def reducestress_scn(self):
        with open('style2.css') as f:
            st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
        selected=option_menu(
            menu_title=None, 
            options=["Home","Heath Score","Excercises","Yoga Asanas","Home Remedies","Reduce Stress","Health Guidelines"],
            icons=("house","coin","controller","emoji-heart-eyes","apple","balloon-heart","hospital"),
            menu_icon="cast",
            default_index=5,
            orientation="horizontal",
        )
        if selected=="Home":
            pass
        
        st.title('PHS Stress Reduction')
        with st.container():
            # st.write("#### Common Cold")
            col1, col2 = st.columns([2,8],gap='small')
            with col1:
                i1=Image.open('./media/welcome/chest.jpg').resize((270,300))
                col1.image(i1)
                
            with col2:
                st.markdown('''<h5>1. Get more physical activity </h5>''',unsafe_allow_html=True)
                st.markdown('''<p>If you're stressed, moving your body consistently may help reduceTrusted Source stress levels and improve mood. A 6-week studyTrusted Source of 185 university students found that participating in aerobic exercise 2 days per week significantly reduced overall perceived stress and perceived stress due to uncertainty. Plus, the exercise routine significantly improved self-reported depression. Regular exercise has been shown to improve symptomsTrusted Source of common mental health conditions such as anxiety and depression (15Trusted Source, 16Trusted Source). If you’re currently inactive, start with gentle activities such as walking or biking. Choosing an activity that you enjoy may help increase your chances of sticking to it in the long term.</p>''',unsafe_allow_html=True)
        with st.container():
            # st.write("#### Common Cold")
            col1, col2 = st.columns([2,8],gap='small')
            with col1:
                i1=Image.open('./media/welcome/chest.jpg').resize((270,300))
                col1.image(i1)
                
            with col2:
                st.markdown('''<h5>2. Eat a balanced diet </h5>''',unsafe_allow_html=True)
                st.markdown('''<p>Your diet affects every aspect of your health, including your mental health. A 2022 review of researchTrusted Source suggests that people who follow a diet high in ultra-processed foods and added sugar are more likely to experience higher perceived stress levels. Being chronically stressed may lead you to overeat and reach for highly palatable foods, which may harm your overall health and mood. Not eating enough nutrient-dense whole foods may increase your risk of deficiencies in nutrients essential for regulating stress and mood, such as magnesium and B vitamins. Minimizing your intake of highly processed foods and beverages and eating more whole foods can help ensure your body is properly nourished. In turn, this may improve your resilience to stress. Whole food options can include: vegetables, fruits, beans, nuts, seeds.</p>''',unsafe_allow_html=True)
        with st.container():
            # st.write("#### Common Cold")
            col1, col2 = st.columns([2,8],gap='small')
            with col1:
                i1=Image.open('./media/welcome/chest.jpg').resize((270,300))
                col1.image(i1)
                
            with col2:
                st.markdown('''<h5>3. Minimize phone use and screen time </h5>''',unsafe_allow_html=True)
                st.markdown('''<p>While smartphones, computers, and tablets are often necessary, using them too often may increase stress levels. A 2021 review of literatureTrusted Source points out that several studies have linked excessive smartphone use with increased stress levels and mental health disorders. Spending too much time in front of screens is associated with lower psychological well-being and increased stress levels in adults and kids. Furthermore, screen time may negatively affect sleep, which may also leadTrusted Source to increased stress levels.</p>''',unsafe_allow_html=True)
        with st.container():
            # st.write("#### Common Cold")
            col1, col2 = st.columns([2,8],gap='small')
            with col1:
                i1=Image.open('./media/welcome/chest.jpg').resize((270,300))
                col1.image(i1)
                
            with col2:
                st.markdown('''<h5>4. Practice self-care </h5>''',unsafe_allow_html=True)
                st.markdown('''<p>Setting aside time to practice self-care may help reduceTrusted Source your stress levels. Practical examples include: going for a walk outside, taking a bath, lighting candles, reading a good book, exercising, preparing a healthy meal, stretching before bed, getting a massage, practicing a hobby, using a diffuser with calming scents, practicing yoga. People who engage in self-care typically haveTrusted Source lower levels of stress and improved quality of life, while a lack of self-care is associated with a higher risk of stress and burnout. Taking time for yourself is essential to live a healthy life. This is especially important for people who tend to be highly stressed, including nurses, doctors, teachers, and caretakers. Self-care doesn’t have to be elaborate or complicated. It simply means tending to your well-being and happiness. Exposure to certain scents via candles or essential oils may be especially calming. Here are a few relaxing scents: lavender, rose, vetiver, bergamot, Roman chamomile, neroli, frankincense, sandalwood, ylang-ylang, orange or orange blossom, geranium. Using scents to boost your mood is called aromatherapy. Aromatherapy can decrease anxiety and improve sleep.</p>''',unsafe_allow_html=True)
        with st.container():
            # st.write("#### Common Cold")
            col1, col2 = st.columns([2,8],gap='small')
            with col1:
                i1=Image.open('./media/welcome/chest.jpg').resize((270,300))
                col1.image(i1)
                
            with col2:
                st.markdown('''<h5>5. Reduce your caffeine intake </h5>''',unsafe_allow_html=True)
                st.markdown('''<p>Caffeine is a chemical in coffee, tea, chocolate, and energy drinks that stimulates your central nervous system. Consuming too much may worsen anxiety, according to a 2021 review of literatureTrusted Source on the subject. Overconsumption may also harm your sleep. In turn, this may increase stress and anxiety symptoms. People have different thresholds for how much caffeine they can tolerate. If caffeine makes you jittery or anxious, consider cutting back by replacing coffee or energy drinks with decaffeinated coffee, herbal tea, or water. though coffee has health benefits in moderation, it's recommended to keep caffeine intake under 400 mgTrusted Source daily, which equals 4–5 cups (0.9–1.2 L) of coffee. Still, people sensitive to caffeine may experience increased anxiety and stress after consuming less caffeine than this, so it's important to consider your tolerance.</p>''',unsafe_allow_html=True)
        with st.container():
            # st.write("#### Common Cold")
            col1, col2 = st.columns([2,8],gap='small')
            with col1:
                i1=Image.open('./media/welcome/chest.jpg').resize((270,300))
                col1.image(i1)
                
            with col2:
                st.markdown('''<h5>6. Spend time with friends and family </h5>''',unsafe_allow_html=True)
                st.markdown('''<p>Social support from friends and family may help you get through stressful times and cope with stress. One 2019 studyTrusted Source in 163 ​​Latinx college-age young adults associated lower levels of support from friends, family, and romantic partners with loneliness, depressive symptoms, and perceived stress. Having a social support system is important for your overall mental health. If you're feeling alone and don't have friends or family to depend on, social support groups may help. Consider joining a club or sports team or volunteering for a cause that's important to you.</p>''',unsafe_allow_html=True)
        with st.container():
            # st.write("#### Common Cold")
            col1, col2 = st.columns([2,8],gap='small')
            with col1:
                i1=Image.open('./media/welcome/chest.jpg').resize((270,300))
                col1.image(i1)
                
            with col2:
                st.markdown('''<h5>7. Create boundaries and learn to say <b>No</b> </h5>''',unsafe_allow_html=True)
                st.markdown('''<p>Not all stressors are within your control, but some are. Putting too much on your plate may increase your stress load and limit the amount of time you can spend on self-care. One way to help reduce stress and protect your mental health may be to say “no” more often. This is especially true if you take on more than you can handle because juggling many responsibilities may leave you feeling overwhelmed. Being selective about what you take on — and saying “no” to things that will unnecessarily add to your load — can reduce your stress levels. Creating boundaries — especially with people who add to your stress levels — is a healthy way to protect your well-being. This can be as simple as asking a friend or family member not to stop by unannounced or canceling standing plans with a friend if you need more space.</p>''',unsafe_allow_html=True)
        with st.container():
            # st.write("#### Common Cold")
            col1, col2 = st.columns([2,8],gap='small')
            with col1:
                i1=Image.open('./media/welcome/chest.jpg').resize((270,300))
                col1.image(i1)
                
            with col2:
                st.markdown('''<h5>8. Avoid procrastination </h5>''',unsafe_allow_html=True)
                st.markdown('''<p>Another way to take control of your stress is to stay on top of your priorities and avoid procrastinating when you aren’t feeling stressed. Procrastination may harm your productivity and leave you scrambling to catch up. This can cause stress, which negatively affects your health and sleep quality. It’s also true that you may be more likelyTrusted Source to procrastinate in times of stress as a coping mechanism. A studyTrusted Source in 140 medical students in China linked procrastination to increased stress levels. The study also associated procrastination and delayed stress reactions with more negative parenting styles, including punishment and rejection. If you find yourself procrastinating regularly, it may be helpful to make a to-do list organized by priority. Give yourself realistic deadlines and work your way down the list. Sometimes, adding an item to the list may help you feel better about it, even if it doesn’t get done immediately. Work on the things that need to get done today, and give yourself chunks of uninterrupted time. Switching between tasks or multitasking can be stressful in itself.</p>''',unsafe_allow_html=True)
        with st.container():
            # st.write("#### Common Cold")
            col1, col2 = st.columns([2,8],gap='small')
            with col1:
                i1=Image.open('./media/welcome/chest.jpg').resize((270,300))
                col1.image(i1)
                
            with col2:
                st.markdown('''<h5>9. Take a yoga class </h5>''',unsafe_allow_html=True)
                st.markdown('''<p>Yoga has become a popular method of stress relief and exercise among all age groups. While yoga styles differ, most share a common goal — to join your body and mind by increasing body and breath awareness. ResearchTrusted Source shows that yoga helps reduce stress and anxiety. Plus, it can promote psychological well-being. These benefits seem related to yoga’s effect on your nervous system and stress response. Yoga may helpTrusted Source lower cortisol levels, blood pressure, and heart rate while increasing levels of gamma aminobutyric acid, a neurotransmitter that’s low in people with mood disorders.</p>''',unsafe_allow_html=True)
        with st.container():
            # st.write("#### Common Cold")
            col1, col2 = st.columns([2,8],gap='small')
            with col1:
                i1=Image.open('./media/welcome/chest.jpg').resize((270,300))
                col1.image(i1)
                
            with col2:
                st.markdown('''<h5>10. Spend time in nature </h5>''',unsafe_allow_html=True)
                st.markdown('''<p>Spending more time outside may help reduce stress. Studies show that spending time in green spaces such as parks and forests and being immersed in nature are healthy ways to manage stress. A review of 14 studiesTrusted Source found that spending as little as 10 minutes in a natural setting may help improve psychological and physiological markers of mental well-being, including perceived stress and happiness, in college-aged people. Hiking and camping are great options, but some people don’t enjoy — or have access to — these activities. Even in an urban area, you can seek out green spaces such as local parks, arboretums, and botanical gardens.</p>''',unsafe_allow_html=True)
                
        pass
    
    def healthguide_scn(self):
        with open('style3.css') as f:
            st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
        selected=option_menu(
            menu_title=None, 
            options=["Home","Heath Score","Excercises","Yoga Asanas","Home Remedies","Reduce Stress","Health Guidelines"],
            icons=("house","coin","controller","emoji-heart-eyes","apple","balloon-heart","hospital"),
            menu_icon="cast",
            default_index=6,
            orientation="horizontal",
        )
        if selected=="Home":
            pass
        
        st.title('PHS Health Guidelines')
        with st.container():
            # st.write("#### Common Cold")
            col1, col2,col3 = st.columns((3),gap='small')
            d={'author': 'TIMESOFINDIA.COM',
               'content': 'In global health, hypertension emerges as a '
                          'prevalent concern, affecting almost 1.28 billion '
                          'adults aged 30–79 years, as per World Health '
                          'Organisation. However, what makes this statistic '
                          'even more no… [+341 chars]',
               'description': 'There is a global prevalence of hypertension, '
                              'particularly among women, and identifies five '
                              'surprising reasons behind it.  The article '
                              'emphasizes lifestyle changes and preventive '
                              'measures to take control of cardiovascular '
                              'health. It encourages a holistic appr…',
               'publishedAt': '2023-11-11T18:30:00Z',
               'source': {'id': 'the-times-of-india',
                          'name': 'The Times of India'},
               'title': '5 shocking reasons behind hypertension seen in women '
                        '- IndiaTimes',
               'url': 'https://timesofindia.indiatimes.com/life-style/health-fitness/health-news/5-shocking-reasons-behind-hypertension-seen-in-women/photostory/105102871.cms',
               'urlToImage': 'https://static.toiimg.com/photo/105102897.cms'}
            img=d['urlToImage']
            title=d['title']
            desc=d['description']
            author=d['author']
            dateofpub=d['publishedAt'][:10]
            url=d['url']
            with col1:
                # i1=Image.open('./media/welcome/chest.jpg').resize((270,300))
                # col1.image(i1)
                col1.markdown(f'''<img src="{img}" alt="Paris" style="width:250px">''',unsafe_allow_html=True)
                col1.markdown(f'''<h4>{title}</h4>''',unsafe_allow_html=True)
                col1.markdown(f'''<b>Desc:</b> {desc}''',unsafe_allow_html=True)
                col1.markdown(f'''<a href="{url}">Read more</a>''',unsafe_allow_html=True)
                col1.markdown(f'''<b>Author: </b><i>{author}</i> <b>Date:</b> <i>{dateofpub}</i>''',unsafe_allow_html=True)
                # col1.markdown('''''',unsafe_allow_html=True)
                # col1.markdown('''''',unsafe_allow_html=True)
            
            with col2:
                # i1=Image.open('./media/welcome/chest.jpg').resize((270,300))
                # col1.image(i1)
                col2.markdown(f'''<img src="{img}" alt="Paris" style="width:250px">''',unsafe_allow_html=True)
                col2.markdown(f'''<h4>{title}</h4>''',unsafe_allow_html=True)
                col2.markdown(f'''<b>Desc:</b> {desc}''',unsafe_allow_html=True)
                col2.markdown(f'''<a href="{url}">Read more</a>''',unsafe_allow_html=True)
                col2.markdown(f'''<b>Author: </b><i>{author}</i> <b>Date:</b> <i>{dateofpub}</i>''',unsafe_allow_html=True)
                # col1.markdown('''''',unsafe_allow_html=True)
                # col1.markdown('''''',unsafe_allow_html=True)
                
            with col3:
                # i1=Image.open('./media/welcome/chest.jpg').resize((270,300))
                # col1.image(i1)
                col3.markdown(f'''<img src="{img}" alt="Paris" style="width:250px">''',unsafe_allow_html=True)
                col3.markdown(f'''<h4>{title}</h4>''',unsafe_allow_html=True)
                col3.markdown(f'''<b>Desc:</b> {desc}''',unsafe_allow_html=True)
                col3.markdown(f'''<a href="{url}">Read more</a>''',unsafe_allow_html=True)
                col3.markdown(f'''<b>Author: </b><i>{author}</i> <b>Date:</b> <i>{dateofpub}</i>''',unsafe_allow_html=True)
                # col1.markdown('''''',unsafe_allow_html=True)
                # col1.markdown('''''',unsafe_allow_html=True)
        pass          


homepage=HomePage()
# homepage.health_check()
# homepage.exercise_rec()
# homepage.yoga()
# homepage.welcome_scn()
# homepage.exercise_scn()
# homepage.yoga_scn()
# homepage.yoga_rec()
# homepage.homeremedies_scn()
# homepage.homeremedies_rec()
# homepage.reducestress_scn()
# homepage.healthguide_scn()
homepage.welcome_scn()