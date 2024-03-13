import streamlit as st 
from PIL import Image 

def convert_image(ima , new_format):
    with Image.open(ima) as image : 
        st.write(ima.name.split('.')[0] + "."+new_format)

        image.save('C:/Users/rohit/Downloads/'+ima.name.split('.')[0] + "."+new_format)




st.title('Image Converter')

ima = st.file_uploader('upload image' , type=['png','jpeg','jpg']) 

new_format = st.selectbox('select which to convert image ' ,options=['png','jpeg','jpg'])

if st.button('convert'):
    if ima is not None:
        convert_image(ima , new_format)
    else:
        st.error('please upload the file')