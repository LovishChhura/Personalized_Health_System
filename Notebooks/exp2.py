import streamlit as st

# Define the image URLs
image_urls = [
    'https://static.streamlit.io/examples/cat.jpg',
    'https://static.streamlit.io/examples/dog.jpg',
    'https://static.streamlit.io/examples/owl.jpg'
]

# Set the number of columns
num_columns = 3

# Display images in columns using HTML
st.markdown('<div style="display: flex; flex-direction: row;">', unsafe_allow_html=True)
for i, url in enumerate(image_urls):
    if i % num_columns == 0 and i != 0:
        st.markdown('</div><div style="display: flex; flex-direction: row;">', unsafe_allow_html=True)
    st.markdown(f'<a href="https://example.com/new_page"><img src="{url}" style="margin: 10px;" width="200"></a>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)



images = ['https://static.streamlit.io/examples/cat.jpg', 'https://static.streamlit.io/examples/dog.jpg', 'https://static.streamlit.io/examples/owl.jpg']
st.image(images, use_column_width=True, caption=["some generic text"] * len(images))