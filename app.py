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
image_url = requests.get('')
app_image = Image.open(BytesIO(image_url.content))
st.image(app_image)

st.markdown('This is an app that you can use to analyze stocks, portfolios and other things in the world of finance\n
    'Use the sidebar for all the modules\n
    'This is a work in progress app.')

