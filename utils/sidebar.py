import streamlit as st


def go_to(page):
    st.session_state.page = page


def render_sidebar(active_page):
    with st.sidebar:
        st.markdown("<div class='sidebar-title'>DashSmartAI</div>", unsafe_allow_html=True)
        st.markdown("<div class='sidebar-subtitle'>Logistics Analytics</div>", unsafe_allow_html=True)

        def nav(label, page):
            class_name = "nav-active" if active_page == page else "nav-item"

            if st.button("", key=page):
                go_to(page)
                st.rerun()

            st.markdown(f"<div class='{class_name}'>{label}</div>", unsafe_allow_html=True)

        nav("Upload Data", "landing")
        nav("Dashboard", "dashboard")
        nav("Predictive Delays", "predictions")

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