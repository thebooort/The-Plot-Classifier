#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 19:29:12 2020

@author: thebooort

Based on the tutorial from pluralsight made by Kimaru Thagana
"""

import streamlit as st
from PIL import Image, ImageOps
import time
st.title("The Plot Classifier")
image1 = Image.open('logoTPC.png')

st.image(image1,caption='Beautiful logo', use_column_width=True)
st.markdown('[![Twitter Follow](https://img.shields.io/twitter/follow/bortizmath.svg?style=social)](https://twitter.com/bortizmath)  ![](https://camo.githubusercontent.com/60dcf2177b53824e7912a6adfb3ff5e318d14ae4/68747470733a2f2f6261646765732e66726170736f66742e636f6d2f6f732f76312f6f70656e2d736f757263652e706e673f763d313033) ![](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) ![](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)')
st.header("The Plot Classifier is an unnecessary deep learning tool, the result of boredom and curiosity. Its goal is to help you find the name of that cool plot/chart you saw on the internet/paper and the most used libraries that can draw it, so you can use it in your research.")
st.text("Pssst, TL;DR:  Just upload a plot image to start")
st.set_option('deprecation.showfileUploaderEncoding', False)
from img_classification import teachable_machine_classification

uploaded_file = st.file_uploader("Choose a plot photo ...", type="jpg")
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    if image.mode != 'RGB':
        image = image.convert('RGB')
    st.image(image, caption='Uploaded Plot.', width=200)
    st.write("")
    st.write("Classifying...")
    with st.spinner('Wait for it...'):
        time.sleep(5)
        st.success('Done!')
    label = teachable_machine_classification(image, 'keras_model.h5')
    if label == 0:
        st.write("Your plot is a.....")
        st.markdown('## Vertical Bar Plot!')
        image2 = Image.open('vertical_bar_plot_success.png')
        st.image(image2, use_column_width=True)
        st.markdown('### Libraries to make this plot:')
        st.markdown('- [matplotlib.pyplot.bar](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.bar.html) ')
        st.markdown('- [Plotly](https://plotly.com/python/bar-charts/)')
        
    else:
        st.write("Your plot is a.....")
        st.markdown('## Horizontal Bar Plot!')


st.markdown('Checkout the code at: [Github]()')

