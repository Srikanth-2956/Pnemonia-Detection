import streamlit as st
from keras.models import load_model
from PIL import Image
import numpy as np
import random
from util import classify, set_background


#set_background('C:/Streamlit app/pneumonia-classification-web-app-python-streamlit-main/pneumonia-classification-web-app-python-streamlit-main/bgs/bg5.png')

# set title
st.title('Pneumonia Detection')

# set header
st.header('Please upload a chest X-ray image')

# upload file
file = st.file_uploader('', type=['jpeg', 'jpg', 'png'])

# load classifier
model = load_model('C:/Streamlit app/pneumonia/model/pneumonia_classifier.h5')

# load class names
with open('C:/Streamlit app/pneumonia/model/labels.txt', 'r') as f:
    class_names = [a[:-1].split(' ')[1] for a in f.readlines()]
    f.close()

# display image
if file is not None:
    image = Image.open(file).convert('RGB')
    st.image(image, use_column_width=True)

    # classify image
    class_name, conf_score = classify(image, model, class_names)

    # write classification
    st.write("## {}".format(class_name))
    st.write("### score: {}%".format(int(conf_score * 1000) / 10))
