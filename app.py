import streamlit as st
from utils.styles import load_css
from views import landing


def main():
    st.set_page_config(
        page_title="DashSmartAI",
        layout="wide"
    )

    st.markdown(load_css(), unsafe_allow_html=True)

    landing.show()


if __name__ == "__main__":
    main()