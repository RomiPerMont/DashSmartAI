import streamlit as st
from utils.styles import load_css
from utils.sidebar import render_sidebar
from views import landing, dashboard, upload, predictions, history, auth

def main():
    st.set_page_config(
        page_title="DashSmartAI",
        layout="wide"
    )

    st.markdown(load_css(), unsafe_allow_html=True)

    # get page from URL
    page = st.query_params.get("page", "landing")

    # routing
    if page == "landing":
        landing.show()

    elif page == "dashboard":
        dashboard.show()

    elif page == "upload":
        upload.show()

    elif page == "predictions":
        predictions.show()

    elif page == "history":
        history.show()

    elif page == "auth":
        auth.show()

    else:
        landing.show()


if __name__ == "__main__":
    main()