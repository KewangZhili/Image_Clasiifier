import streamlit as st
import tensorflow as tf
class_names = ['Fake','Real']
modelp=tf.keras.models.load_model('my_model2.hdf5')
st.write(
         """
         # AI-Real Image Classification
         """
         )

file = st.file_uploader("Please upload image to check if its real or ai generated", type=["jpg", "png"])
from PIL import Image, ImageOps
import numpy as np
def import_and_predict(image_data, model1):
        size = (32,32)    
        image = ImageOps.fit(image_data, size, Image.ANTIALIAS)
        image = np.asarray(image)
        img_reshape = image[np.newaxis,...]#model is trained on 4dimensions,this line adds new dimension
        prediction = model1.predict(img_reshape)        
        return prediction

if file is None:
    st.text("Please upload an image file")
else:
    image = Image.open(file)
    st.image(image, use_column_width=True)#display 
    predictions = import_and_predict(image, modelp)
    score = tf.nn.sigmoid(predictions[0])
    #st.write(predictions[0])
    #st.write(score)
    if(predictions[0]==0):
             st.write("This image is most likely AI-Generated.")
    else:
             st.write("This image is most likely Real.")

