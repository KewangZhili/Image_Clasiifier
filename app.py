import streamlit as st
import tensorflow as tf
st.set_option('deprecation.showfileUploaderEncoding',False)
class_names = ['Fake','Real']
@st.cache_data#so that we dont need to load the model each time
def load_model():
  model=tf.keras.models.load_model('my_model2.hdf5')
  return model


with st.spinner('Model is being loaded..'):
  model=load_model()

st.write(
         """
         # AI-Real Image Classification
         """
         )

file = st.file_uploader("Please upload image to check if its real or ai generated", type=["jpg", "png"])
from PIL import Image, ImageOps
import numpy as np
def import_and_predict(image_data, model):
        size = (32,32)    
        image = ImageOps.fit(image_data, size, Image.ANTIALIAS)
        image = np.asarray(image)
        img_reshape = imgage[np.newaxis,...]#model is trained on 4dimensions,this line adds new dimension
        prediction = model.predict(img_reshape)        
        return prediction

if file is None:
    st.text("Please upload an image file")
else:
    image = Image.open(file)
    st.image(image, use_column_width=True)#display 
    predictions = import_and_predict(image, model)
    score = tf.nn.sigmoid(predictions[0])
    st.write(predictions)
    st.write(score)
    print(
    "This image most likely belongs to {} with a {:.2f} percent confidence."
    .format(class_names[np.argmax(score)], 100 * np.max(score))
)

