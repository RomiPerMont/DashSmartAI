import streamlit as st


def render_sidebar(active_page):
    with st.sidebar:
        st.markdown("<div class='sidebar-title'>DashSmartAI</div>", unsafe_allow_html=True)
        st.markdown("<div class='sidebar-subtitle'>Logistics Analytics</div>", unsafe_allow_html=True)

        def nav_item(label, page_name):
            class_name = "nav-active" if active_page == page_name else "nav-item"

            st.markdown(
                f"<a class='{class_name}' href='?page={page_name}'>{label}</a>",
                unsafe_allow_html=True
            )

        nav_item("Upload Data", "landing")
        nav_item("Dashboard", "dashboard")
        nav_item("Predictive Delays", "predictions")

        st.markdown("<div class='sidebar-divider'></div>", unsafe_allow_html=True)

        st.markdown(
            """
            <div class='login-register-row'>
                <div class='login-button'>Login</div>
                <div class='register-button'>Register</div>
            </div>
            """,
            unsafe_allow_html=True,
        )