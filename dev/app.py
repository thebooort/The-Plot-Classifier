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


def print_info(label):
    if label == 0:
        st.write("Your plot is a.....")
        st.markdown('## Vertical Bar Plot!')
        image2 = Image.open('vertical_bar_plot_success.png')
        st.image(image2, use_column_width=True)
        st.markdown('### Libraries to make this plot:')
        st.markdown('- [matplotlib.pyplot.bar](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.bar.html) ')
        st.markdown('- [Plotly](https://plotly.com/python/bar-charts/)')
 
    elif label == 1:
            st.write("Your plot is a.....")
            st.markdown('## Horizontal Bar Plot!')
            image2 = Image.open('horizontal_bar_plot_success.png')
            st.image(image2, use_column_width=True)
            st.markdown('### Libraries to make this plot:')
            st.markdown('- [matplotlib.pyplot.bar](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.bar.html) ')
            st.markdown('- [Plotly](https://plotly.com/python/bar-charts/)') 
        
    elif label == 2:
            st.write("Your plot is a.....")
            st.markdown('## Scatter Plot!')
            image2 = Image.open('scatter_plot_success.png')
            st.image(image2, use_column_width=True)
            st.markdown('### Libraries to make this plot:')
            st.markdown('- [matplotlib.pyplot.bar](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.bar.html) ')
            st.markdown('- [Plotly](https://plotly.com/python/bar-charts/)')

    elif label == 3:
            st.write("Your plot is a.....")
            st.markdown('## Area Plot!')
            image2 = Image.open('area_plot_success.png')
            st.image(image2, use_column_width=True)
            st.markdown('### Libraries to make this plot:')
            st.markdown('- [matplotlib.pyplot.bar](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.bar.html) ')
            st.markdown('- [Plotly](https://plotly.com/python/bar-charts/)')
        
    elif label == 4:
            st.write("Your plot is a.....")
            st.markdown('## Box Plot!')
            image2 = Image.open('box_plot_success.png')
            st.image(image2, use_column_width=True)
            st.markdown('### Libraries to make this plot:')
            st.markdown('- [matplotlib.pyplot.bar](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.bar.html) ')
            st.markdown('- [Plotly](https://plotly.com/python/bar-charts/)')
        
    elif label == 5:
            st.write("Your plot is a.....")
            st.markdown('## Bubble Plot!')
            image2 = Image.open('Bubble_plot_success.png')
            st.image(image2, use_column_width=True)
            st.markdown('### Libraries to make this plot:')
            st.markdown('- [matplotlib.pyplot.bar](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.bar.html) ')
            st.markdown('- [Plotly](https://plotly.com/python/bar-charts/)')
        
    elif label == 6:
            st.write("Your plot is a.....")
            st.markdown('## Chord Plot!')
            image2 = Image.open('Chord_plot_success.png')
            st.image(image2, use_column_width=True)
            st.markdown('### Libraries to make this plot:')
            st.markdown('- [matplotlib.pyplot.bar](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.bar.html) ')
            st.markdown('- [Plotly](https://plotly.com/python/bar-charts/)')
        
    elif label == 7:
            st.write("Your plot is a.....")
            st.markdown('## Choropleth Plot!')
            image2 = Image.open(' Choropleth_plot_success.png')
            st.image(image2, use_column_width=True)
            st.markdown('### Libraries to make this plot:')
            st.markdown('- [matplotlib.pyplot.bar](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.bar.html) ')
            st.markdown('- [Plotly](https://plotly.com/python/bar-charts/)')
        
    elif label == 8:
            st.write("Your plot is a.....")
            st.markdown('## Demographic Pyramid!')
            image2 = Image.open('demographic_pyramid_plot_success.png')
            st.image(image2, use_column_width=True)
            st.markdown('### Libraries to make this plot:')
            st.markdown('- [matplotlib.pyplot.bar](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.bar.html) ')
            st.markdown('- [Plotly](https://plotly.com/python/bar-charts/)')
        
    elif label == 9:
            st.write("Your plot is a.....")
            st.markdown('## Doughnut Plot!')
            image2 = Image.open('doughnut_plot_success.png')
            st.image(image2, use_column_width=True)
            st.markdown('### Libraries to make this plot:')
            st.markdown('- [matplotlib.pyplot.bar](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.bar.html) ')
            st.markdown('- [Plotly](https://plotly.com/python/bar-charts/)')
        
    elif label == 10:
            st.write("Your plot is a.....")
            st.markdown('## Line Plot!')
            image2 = Image.open('line_plot_success.png')
            st.image(image2, use_column_width=True)
            st.markdown('### Libraries to make this plot:')
            st.markdown('- [matplotlib.pyplot.bar](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.bar.html) ')
            st.markdown('- [Plotly](https://plotly.com/python/bar-charts/)')
        
    elif label == 11:
            st.write("Your plot is a.....")
            st.markdown('## Pie Plot!')
            image2 = Image.open('pie_plot_success.png')
            st.image(image2, use_column_width=True)
            st.markdown('### Libraries to make this plot:')
            st.markdown('- [matplotlib.pyplot.bar](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.bar.html) ')
            st.markdown('- [Plotly](https://plotly.com/python/bar-charts/)')
        
    elif label == 12:
            st.write("Your plot is a.....")
            st.markdown('## Spider Plot!')
            image2 = Image.open('spider_plot_success.png')
            st.image(image2, use_column_width=True)
            st.markdown('### Libraries to make this plot:')
            st.markdown('- [matplotlib.pyplot.bar](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.bar.html) ')
            st.markdown('- [Plotly](https://plotly.com/python/bar-charts/)')
        
    elif label == 13:
            st.write("Your plot is a.....")
            st.markdown('## Violin Plot!')
            image2 = Image.open('violin_plot_success.png')
            st.image(image2, use_column_width=True)
            st.markdown('### Libraries to make this plot:')
            st.markdown('- [matplotlib.pyplot.bar](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.bar.html) ')
            st.markdown('- [Plotly](https://plotly.com/python/bar-charts/)')




st.title("The Plot Classifier")
image1 = Image.open('logoTPC.png')

st.image(image1,caption='Beautiful logo', use_column_width=True)
st.markdown('[![Twitter Follow](https://img.shields.io/twitter/follow/bortizmath.svg?style=social)](https://twitter.com/bortizmath)  ![](https://camo.githubusercontent.com/60dcf2177b53824e7912a6adfb3ff5e318d14ae4/68747470733a2f2f6261646765732e66726170736f66742e636f6d2f6f732f76312f6f70656e2d736f757263652e706e673f763d313033) ![](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) ![](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat) ![](https://camo.githubusercontent.com/b0a36dc1ea0e417823a1ba090f282b8e4a928c86/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f6c6963656e73652f746865626f6f6f72742f5468652d506c6f742d436c6173736966696572)')
st.header("The Plot Classifier is an unnecessary deep learning tool, the result of boredom and curiosity. Its goal is to help you find the name of that cool plot/chart you saw on the internet/paper and the most used libraries that can draw it, so you can use it in your research.")
st.text("Pssst, TL;DR:  Just upload a plot image to start")
st.set_option('deprecation.showfileUploaderEncoding', False)
from img_classification import teachable_machine_classification

uploaded_file = st.file_uploader("Choose a plot photo ...")
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
    print_info(label)


st.markdown('Checkout the code at: [Github]()')
