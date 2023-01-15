import streamlit as st
import requests
from io import BytesIO #BytesIO
from io import StringIO #StringIO
import http.client #API
import os #operating system functions
from PIL import Image #open pictures

st.title(':moneybag: FINANCE APP :moneybag:')

#image
image_url = requests.get('https://raw.githubusercontent.com/IIPeteII/Finance/blob/67d9f1c2f51d24e3faa53ebf0d9018e09ef34a85/images/bull.jpg')
app_image = Image.open(BytesIO(image_url.content))
st.image(app_image)

st.markdown('This is an app that you can use to analyze stocks, portfolios and other things in the world of finance\
    Use the sidebar for all the modules\
    This is a work in progress app.')

