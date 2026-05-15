import streamlit as st
from utils.sidebar import render_sidebar

def show():
    
    st.markdown("<div class='page-title'>Predictive Delays</div>", unsafe_allow_html=True)
    st.write("Prediction results will go here.")