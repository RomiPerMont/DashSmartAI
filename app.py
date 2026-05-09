import streamlit as st
from utils.styles import load_css
from views import landing, dashboard, upload, predictions, history, auth


def main():
    st.set_page_config(
        page_title="DashSmartAI",
        layout="wide"
    )

    st.markdown(load_css(), unsafe_allow_html=True)

if "page" not in st.session_state:
        st.session_state.page = "landing"

        if st.session_state.page == "landing":
            landing.show()
        elif st.session_state.page == "dashboard":
            dashboard.show()
        elif st.session_state.page == "upload":
            upload.show()
        elif st.session_state.page == "predictions":
            predictions.show()
        elif st.session_state.page == "history":
            history.show()
        elif st.session_state.page == "auth":
            auth.show()

if __name__ == "__main__":
    main()