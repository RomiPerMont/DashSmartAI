import streamlit as st
import pandas as pd
import plotly.express as px


def get_data():
    if "uploaded_df" in st.session_state:
        return st.session_state.uploaded_df

    if "df" in st.session_state:
        return st.session_state.df

    return None


def find_column(df, possible_names):
    for col in df.columns:
        clean_col = col.lower().replace(" ", "_")
        for name in possible_names:
            if name in clean_col:
                return col
    return None


def show():

    # temporary check to see if the uploaded csv is saved
    st.write(st.session_state)

    st.markdown(
        """
        <div class="page-header">
            <h1>Dashboard Overview</h1>
            <p>Logistics performance metrics and delivery insights</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    df = get_data()

    if df is None:
        st.warning("Upload a CSV file first to view the dashboard.")
        return

    total_deliveries = len(df)

    status_col = find_column(df, ["status", "delivery_status"])
    delay_col = find_column(df, ["delay", "delay_time", "delay_hours"])
    route_col = find_column(df, ["route", "route_name"])
    date_col = find_column(df, ["date", "delivery_date"])

    if status_col:
        on_time_count = df[status_col].astype(str).str.lower().str.contains("on").sum()
        on_time_rate = round((on_time_count / total_deliveries) * 100, 1)
    elif delay_col:
        on_time_count = (pd.to_numeric(df[delay_col], errors="coerce").fillna(0) <= 0).sum()
        on_time_rate = round((on_time_count / total_deliveries) * 100, 1)
    else:
        on_time_rate = 0

    if delay_col:
        avg_delay = round(pd.to_numeric(df[delay_col], errors="coerce").fillna(0).mean(), 1)
    else:
        avg_delay = 0

    if route_col:
        active_routes = df[route_col].nunique()
    else:
        active_routes = 0

    high_risk = int(total_deliveries - on_time_count) if "on_time_count" in locals() else 0

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.markdown(
            f"""
            <div class="kpi-card">
                <div class="kpi-icon green">↑</div>
                <p>On-Time Delivery Rate</p>
                <h2>{on_time_rate}%</h2>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with col2:
        st.markdown(
            f"""
            <div class="kpi-card">
                <div class="kpi-icon orange">⏱</div>
                <p>Average Delay Time</p>
                <h2>{avg_delay}h</h2>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with col3:
        st.markdown(
            f"""
            <div class="kpi-card">
                <div class="kpi-icon blue">📦</div>
                <p>Total Deliveries</p>
                <h2>{total_deliveries}</h2>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with col4:
        st.markdown(
            f"""
            <div class="kpi-card">
                <div class="kpi-icon purple">📍</div>
                <p>Active Routes</p>
                <h2>{active_routes}</h2>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown("<br>", unsafe_allow_html=True)

    chart_col1, chart_col2 = st.columns(2)

    with chart_col1:
        st.markdown("<div class='chart-card'>", unsafe_allow_html=True)
        st.subheader("Delivery Status")

        if status_col:
            status_data = df[status_col].value_counts().reset_index()
            status_data.columns = ["Status", "Count"]

            fig = px.pie(
                status_data,
                names="Status",
                values="Count",
                hole=0.45,
            )

            fig.update_layout(
                height=350,
                margin=dict(l=20, r=20, t=30, b=20),
                showlegend=True,
            )

            st.plotly_chart(fig, use_container_width=True)
        else:
            st.info("No status column found in this dataset.")

        st.markdown("</div>", unsafe_allow_html=True)

    with chart_col2:
        st.markdown("<div class='chart-card'>", unsafe_allow_html=True)
        st.subheader("Route Performance")

        if route_col and delay_col:
            route_data = (
                df.groupby(route_col)[delay_col]
                .mean()
                .reset_index()
                .sort_values(by=delay_col, ascending=True)
            )

            fig = px.bar(
                route_data,
                x=route_col,
                y=delay_col,
                labels={route_col: "Route", delay_col: "Average Delay"},
            )

            fig.update_layout(
                height=350,
                margin=dict(l=20, r=20, t=30, b=20),
            )

            st.plotly_chart(fig, use_container_width=True)
        else:
            st.info("No route or delay column found in this dataset.")

        st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown(
        f"""
        <div class="summary-card">
            <h3>Performance Summary</h3>
            <p><strong>{total_deliveries}</strong> records were analysed.</p>
            <p><strong>{high_risk}</strong> deliveries may need attention.</p>
            <p>This dashboard helps users understand delivery performance before moving to predictive delay analysis.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("<br>", unsafe_allow_html=True)

    st.dataframe(df, use_container_width=True)