# pages/history.py
import streamlit as st
import pandas as pd

def render_history_page():

    st.title("Analysis History")

    # simulate user logged in 
    user_logged_in = True  

    if not user_logged_in:
        st.warning("Login required to access analysis history.")
        return

    # sample data 
    data = {
        "File Name": ["data1.csv", "routes.csv"],
        "Date": ["2026-05-10", "2026-05-08"],
        "Records": [1200, 850],
        "Model Accuracy": ["82%", "78%"],
        "High Risk Deliveries": [45, 30]
    }

    df = pd.DataFrame(data)

    st.dataframe(df, use_container_width=True)

    st.subheader("Actions")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.button("View Results")

    with col2:
        st.button("Export")

    with col3:
        st.button("Delete")