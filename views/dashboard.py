import streamlit as st
from utils.sidebar import render_sidebar

def show():
    render_sidebar("dashboard")

    st.markdown("<div class='page-title'>Dashboard</div>", unsafe_allow_html=True)
    st.write("Dashboard page content will go here.")