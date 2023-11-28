#%%
import pandas as pd
import streamlit as st
from datetime import date
from model_mine import get_prediction
from PIL import Image
import os
#%%


    
image_ice = Image.open('img/Iceberg-Data-Final-Logo.png')
image_procol = Image.open('img/reCaptcha.png')


col1, col2, col3 = st.columns(3)

with col1:
    st.image(image_procol, width=150, use_column_width=True)

with col2:
    # Add content to the second column if desired
    pass

with col3:
    st.image(image_ice, width=150, use_column_width=True)

# st.header("*Kiruna*")# - Extractor de información de propiedades")
st.header("Tool to solve reCaptcha blockers")
st.write("Upload the image that you want to solve and the tool will return the text in the image")
# st.write("Bogotá y Soacha")
st.write('***')
#st.write('**Inputs**')

# Imgae uploader
st.title("Image Uploader")
uploaded_file = st.file_uploader("Choose an image...", type=["jpg","webp","jpeg"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    # st.image(image, caption='Uploaded Image.', use_column_width=True)

    # Get the directory path of the script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Save the uploaded image with the same name in the same folder
    uploaded_filename = os.path.join(script_dir, uploaded_file.name)
    image.save(uploaded_filename)
    print("Image saved as: ", uploaded_filename)
    prediction = get_prediction(uploaded_filename)
    st.write("Here is the prediction:")
    st.image(prediction, caption='Prediction Result', use_column_width=True)
    
else:
    st.write('No image uploaded')

