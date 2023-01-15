#COMMON
import pandas as pd #DF work
import numpy as np #Functions
import matplotlib.pyplot as plt #Visualizations
import requests
import altair as alt #Visualizations
import io #Buffers for DF's
from io import BytesIO #BytesIO
from io import StringIO #StringIO
import http.client #API
import os #operating system functions
from PIL import Image #open pictures
from pathlib import Path #path function
from scipy.io import loadmat #load .mat files
import datetime #dates and time stuff
import json

#uploading/file management
from tempfile import NamedTemporaryFile

#Deployment
import streamlit as st #app deployment


st.title(':moneybag: FINANCE APP :moneybag:')

#image
image_url = requests.get('https://raw.githubusercontent.com/IIPeteII/Finance/main/images/gold-bull.jpg')
app_image = Image.open(BytesIO(image_url.content))
st.image(app_image)

st.markdown('This is an app that _regonizes_ and **detects** license plates in images, then return an image of the car model.\
    The app takes the string of the license plate and searches for it in the Danish license plate database, which then returns information such as brand, model and year.\
    Thereafter, the app goes through a large dataset of car models and returns an image of the car, if the car is not in the dataset - a google search is performed.')
