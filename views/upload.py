import streamlit as st
import pandas as pd


def show():

    st.title("Upload Logistics Data")

    # create history list
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

        # save dataframe for dashboard and predictions pages
        st.session_state.uploaded_df = df

        # save upload into history
        st.session_state.history.append({
            "file_name": uploaded_file.name,
            "date": pd.Timestamp.now().strftime("%Y-%m-%d"),
            "records": len(df),
            "accuracy": "80%",   # later connect model accuracy
            "high_risk": 10      # later connect predictions
        })

        # success message
        st.success("File uploaded successfully!")

        # explain uploaded dataset
        st.info(
            "This dataset is now available for dashboard analytics "
            "and predictive delay analysis."
        )

        # preview title
        st.subheader("Dataset Preview")

        # explain preview table
        st.caption(
            "This preview shows the first rows of the uploaded logistics dataset."
        )

        # preview dataframe
        st.dataframe(df.head(), use_container_width=True)

        # dataset summary
        st.subheader("Dataset Summary")

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric("Total Records", len(df))

        with col2:
            st.metric("Columns", len(df.columns))

        with col3:
            st.metric("Missing Values", df.isnull().sum().sum())

        # explain summary cards
        st.caption(
            "These blocks help users quickly understand the uploaded data quality."
        )