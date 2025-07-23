import streamlit as st
import pandas as pd
import numpy as np

st.header("Streamlit Day 2")
st.progress(85)
st.color_picker("pick a color")
st.image("images/the bad guys.jpg", None)
#Creating a side bar
st.sidebar.title("login here")
st.sidebar.text_input("Username")
st.sidebar.text_input("password", type= "password")
st.sidebar.file_uploader("Upload a file")
st.sidebar.image("images/submit.png", None, 100)