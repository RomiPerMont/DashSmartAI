def load_css():
    return """
    <style>

    .stApp {
        background-color: #f8fafc;
    }

    .block-container {
        padding-top: 2rem;
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
        font-size: 26px;
        font-weight: 700;
        color: #2563eb;
        margin-bottom: 5px;
    }

    .sidebar-subtitle {
        font-size: 16px;
        color: #6b7280;
        margin-bottom: 35px;
    }

    /* ACTIVE ITEM */
    .nav-active {
        display: block;
        text-decoration: none !important;
        background-color: #eff6ff;
        color: #2563eb !important;

        padding: 14px 18px;
        border-radius: 12px;
        font-size: 18px;
        font-weight: 700;
        margin-bottom: 18px;
    }

    /* NORMAL ITEM */
    .nav-item {
        display: block;
        text-decoration: none !important;
        color: #1f2937 !important;

        padding: 14px 18px;
        border-radius: 12px;
        font-size: 18px;
        font-weight: 700;
        margin-bottom: 18px;
    }

    /* HOVER */
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
        display: block;
        border: 1px solid #d1d5db;
        color: #1f2937;
        background-color: #ffffff;
        padding: 14px 18px;
        border-radius: 12px;
        font-size: 16px;
        font-weight: 600;
        width: 48%;
        text-align: center;
    }

    .register-button {
        display: block;
        color: white;
        background-color: #2563eb;
        padding: 14px 18px;
        border-radius: 12px;
        font-size: 16px;
        font-weight: 600;
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

    </style>
    """