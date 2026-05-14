import streamlit as st
import pandas as pd


def show():

    st.title("Upload Logistics Data")

    # create history list if it does not exist
    if "history" not in st.session_state:
        st.session_state.history = []

    # upload csv file
    uploaded_file = st.file_uploader(
        "Upload CSV File",
        type=["csv"]
    )

    # when user uploads a file
    if uploaded_file:

        # read csv
        df = pd.read_csv(uploaded_file)

        # save upload into history
        st.session_state.history.append({
            "file_name": uploaded_file.name,
            "date": pd.Timestamp.now().strftime("%Y-%m-%d"),
            "records": len(df),
            "accuracy": "80%",   # later connect model accuracy
            "high_risk": 10      # later connect predictions
        })

        st.success("File uploaded successfully!")

        # preview data
        st.subheader("Dataset Preview")
        st.dataframe(df.head(), use_container_width=True)