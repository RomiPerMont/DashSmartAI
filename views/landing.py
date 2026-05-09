import streamlit as st
from utils.sidebar import render_sidebar

def nav_item(label, page_name):
    is_active = st.session_state.page == page_name
    class_name = "nav-active" if is_active else "nav-item"

    if st.button("", key=f"nav_{page_name}"):
        st.session_state.page = page_name
        st.rerun()

    st.markdown(
        f"<div class='{class_name}'>{label}</div>",
        unsafe_allow_html=True
    )


def render_upload_requirements():
    st.markdown(
        """
        <div class='info-card'>
            <div class='info-title'>Data Requirements</div>
            <div class='info-text'>
                CSV file format with headers<br>
                Required columns: delivery_id, route, departure_time, arrival_time, status<br>
                Maximum file size: 50MB<br>
                Date format: YYYY-MM-DD HH:MM:SS
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_upload_visual():
    st.markdown(
        """
        <div class='upload-card'>
            <div class='upload-box'>
                <div class='upload-circle'>↑</div>
                <div class='upload-title'>Drop your CSV file here</div>
                <div class='upload-subtitle'>or click to browse</div>
                <div class='select-file-button'>Select File</div>
                <div class='support-text'>Supports: CSV files only</div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def show():
    render_sidebar("landing")

    st.markdown("<div class='page-title'>Upload Data</div>", unsafe_allow_html=True)
    st.markdown(
        "<div class='page-subtitle'>Import your logistics CSV data for analysis</div>",
        unsafe_allow_html=True,
    )

    render_upload_requirements()
    render_upload_visual()

    uploaded_file = st.file_uploader(
        "Upload CSV",
        type=["csv"],
        label_visibility="collapsed"
    )

    if uploaded_file:
        st.success("File selected")
        st.write(uploaded_file.name)

    st.button("Process Data", use_container_width=True)