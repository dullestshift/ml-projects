import streamlit as st
import pickle
from PIL import Image




if st.button("Home"):
    st.switch_page("home.py")
if st.button("check your mental health"):
    st.switch_page("pred.py")
