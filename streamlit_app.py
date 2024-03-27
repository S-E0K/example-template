import streamlit as st
import numpy as np
import pandas as pd
import altair as alt

# Page title
st.set_page_config(page_title='Interactive Data Explorer', page_icon='📊')
st.title('📊 Interactive Data Explorer')

st.sidebar.title('sidebar title')


st.title("title")
st.header("header")
st.markdown("markdown")
st.subheader("subheader")
st.caption("caption")
st.code("x=2021")
st.latex(r''' a+a r^1+a r^2+a r^3 ''')


st.image('https://i.namu.wiki/i/GipPGXXN_yW6nfeWCZ3Ba4QCDzSy50yVIc5GwewwM_2HDQeujYH5xq0CqWxsRu0GhKRq_VzUwKzM4tmKoya0nQ.webp')

st.checkbox('yes')
st.button('Click')
gender = st.radio('Pick gender', ['male', 'female'])
st.selectbox('Pick gender', ['male', 'female'])
planet = st.multiselect('choose a planet', ['jupiter', 'mars', 'earth'])
st.select_slider('Pick a mark', ['Bad', 'Good'])
x = st.slider('Pick a number', 0, 50)


st.write('성별', gender)
st.write('행성', planet)

st.number_input('Pick a number', 0, 10)
st.text_input('Email address')
st.date_input('Travelling date')
st.time_input('School time')
st.text_area('Description')
st.file_uploader('Update a photo')
color = st.color_picker('Choose your favorite color')












