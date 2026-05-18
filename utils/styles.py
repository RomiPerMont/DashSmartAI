def load_css():
    return """
    <style>

    .stApp {
        background-color: #f8fafc;
    }

    .block-container {
        padding-top: 4rem;
        padding-left: 3rem;
        padding-right: 3rem;
        max-width: 1200px;
    }

    section[data-testid="stSidebar"] {
        background-color: #ffffff;
        border-right: 1px solid #e5e7eb;
    }

    section[data-testid="stSidebar"] > div {
        padding-top: 1.5rem;
    }

    .sidebar-title {
        font-size: 40px;
        font-weight: 700;
        color: #2563eb;
        margin-bottom: 5px;
    }

    .sidebar-subtitle {
        font-size: 18px;
        color: #6b7280;
        margin-bottom: 35px;
    }

    .nav-active {
        display: block;
        text-decoration: none !important;
        background-color: #eff6ff;
        color: #2563eb !important;
        padding: 14px 18px;
        border-radius: 12px;
        font-size: 22px;
        font-weight: 400;
        margin-bottom: 18px;
    }

    .nav-item {
        display: block;
        text-decoration: none !important;
        color: #1f2937 !important;
        padding: 14px 18px;
        border-radius: 12px;
        font-size: 22px;
        font-weight: 400;
        margin-bottom: 18px;
    }

    .nav-item:hover,
    .nav-active:hover {
        background-color: #eff6ff;
        color: #2563eb !important;
        text-decoration: none !important;
    }

    .sidebar-divider {
        border-top: 1px solid #e5e7eb;
        margin-top: 25px;
        margin-bottom: 20px;
    }

    .login-register-row {
        display: flex;
        gap: 10px;
    }

    .login-button {
        border: 1px solid #d1d5db;
        color: #2563eb;
        background-color: #ffffff;
        padding: 14px 18px;
        border-radius: 12px;
        font-size: 16px;
        font-weight: 400;
        width: 48%;
        text-align: center;
    }

    .register-button {
        color: white;
        background-color: #2563eb;
        padding: 14px 18px;
        border-radius: 12px;
        font-size: 16px;
        font-weight: 400;
        width: 48%;
        text-align: center;
    }

    .page-title {
        font-size: 38px;
        font-weight: 700;
        color: #111827;
        margin-bottom: 2px;
    }

    .page-subtitle {
        font-size: 20px;
        color: #4b5563;
        margin-bottom: 40px;
    }

    .info-card {
        background-color: #eff6ff;
        border: 1px solid #bfdbfe;
        border-radius: 16px;
        padding: 28px;
        margin-bottom: 30px;
    }

    .info-title {
        color: #1e3a8a;
        font-size: 22px;
        font-weight: 700;
        margin-bottom: 20px;
    }

    .info-text {
        color: #1d4ed8;
        font-size: 16px;
        line-height: 2;
    }

    .upload-card {
        background-color: white;
        border: 1px solid #e5e7eb;
        border-radius: 16px;
        padding: 40px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.08);
    }

    .upload-box {
        border: 2px dashed #cbd5e1;
        background-color: #f9fafb;
        border-radius: 16px;
        padding: 70px 40px;
        text-align: center;
    }

    .upload-circle {
        width: 82px;
        height: 82px;
        background-color: #dbeafe;
        border-radius: 50%;
        margin: auto;
        margin-bottom: 26px;
        display: flex;
        align-items: center;
        justify-content: center;
        color: #2563eb;
        font-size: 40px;
    }

    .upload-title {
        font-size: 24px;
        font-weight: 700;
        color: #111827;
        margin-bottom: 15px;
    }

    .upload-subtitle {
        font-size: 20px;
        color: #4b5563;
        margin-bottom: 25px;
    }

    .select-file-button {
        background-color: #2563eb;
        color: white;
        padding: 12px 28px;
        border-radius: 12px;
        font-size: 18px;
        font-weight: 600;
        display: inline-block;
        margin-top: 10px;
    }

    .support-text {
        font-size: 16px;
        color: #6b7280;
        margin-top: 15px;
    }

    div[data-testid="stFileUploader"] {
        display: none;
    }

    .stButton > button {
        background-color: #d1d5db;
        color: white;
        border: none;
        border-radius: 12px;
        padding: 14px;
        font-size: 18px;
        font-weight: 600;
    }
        /* =========================
PAGE HEADER
this is the top title area of the dashboard page
example:
Dashboard Overview
Logistics performance metrics and delivery insights
========================= */
.page-header {
    margin-bottom: 25px;
}

/* main dashboard title */
.page-header h1 {
    font-size: 34px;
    font-weight: 800;
    color: #111827;
    margin-bottom: 5px;
}

/* small subtitle under the title */
.page-header p {
    color: #6b7280;
    font-size: 16px;
}


/* =========================
KPI CARDS
these are the top statistic cards
example:
on-time delivery %
average delay
total deliveries
active routes
========================= */
.kpi-card {
    background: white;
    padding: 22px;
    border-radius: 18px;
    border: 1px solid #e5e7eb;
    box-shadow: 0 6px 20px rgba(15, 23, 42, 0.06);
    min-height: 160px;
}

/* text inside kpi cards
example:
On-Time Delivery Rate
*/
.kpi-card p {
    color: #6b7280;
    font-size: 14px;
    margin-top: 14px;
    margin-bottom: 5px;
}

/* big numbers inside kpi cards
example:
82%
1200
*/
.kpi-card h2 {
    color: #111827;
    font-size: 32px;
    font-weight: 800;
    margin: 0;
}


/* =========================
KPI ICON BOXES
small colored square behind icons
========================= */
.kpi-icon {
    width: 46px;
    height: 46px;
    border-radius: 14px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-weight: 800;
}


/* green card icon
used for positive results */
.green {
    background: #dcfce7;
    color: #16a34a;
}

/* orange card icon
used for delay times */
.orange {
    background: #ffedd5;
    color: #ea580c;
}

/* blue card icon
used for deliveries */
.blue {
    background: #dbeafe;
    color: #2563eb;
}

/* purple card icon
used for route information */
.purple {
    background: #ede9fe;
    color: #7c3aed;
}


/* =========================
CHART CONTAINERS
this is the white box around charts
example:
pie chart
bar chart
========================= */
.chart-card {
    background: white;
    padding: 22px;
    border-radius: 18px;
    border: 1px solid #e5e7eb;
    box-shadow: 0 6px 20px rgba(15, 23, 42, 0.06);
}


/* =========================
SUMMARY SECTION
bottom information box
example:
performance summary
========================= */
.summary-card {
    background: linear-gradient(135deg, #ecfeff, #f0fdf4);
    border: 1px solid #ccfbf1;
    border-radius: 18px;
    padding: 24px;
}

/* summary title */
.summary-card h3 {
    color: #111827;
    font-size: 22px;
    font-weight: 800;
    margin-bottom: 10px;
}

/* summary text */
.summary-card p {
    color: #374151;
    margin-bottom: 6px;
}
    </style>
    """