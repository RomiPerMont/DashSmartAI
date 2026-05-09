def load_css():
    return """
    <style>

    /* general app background */
    .stApp {
        background-color: #f8fafc;
    }

    /* main page spacing */
    .block-container {
        padding-top: 2rem;
        padding-left: 3rem;
        padding-right: 3rem;
        max-width: 1200px;
    }

    /* sidebar background */
    section[data-testid="stSidebar"] {
        background-color: #ffffff;
        border-right: 1px solid #e5e7eb;
    }

    /* sidebar spacing */
    section[data-testid="stSidebar"] > div {
        padding-top: 1.5rem;
    }

    /* title */
    .sidebar-title {
        font-size: 26px;
        font-weight: 700;
        color: #2563eb;
        margin-bottom: 5px;
    }

    /* subtitle */
    .sidebar-subtitle {
        font-size: 16px;
        color: #6b7280;
        margin-bottom: 35px;
    }

    /* active menu item */
    .nav-active {
        background-color: #eff6ff;
        color: #2563eb;
        padding: 14px 18px;
        border-radius: 12px;
        font-size: 18px;
        font-weight: 700;
        margin-bottom: 18px;
    }

    /* normal menu item */
    .nav-item {
        color: #1f2937;
        padding: 14px 18px;
        border-radius: 12px;
        font-size: 18px;
        font-weight: 700;
        margin-bottom: 18px;
    }

    /* divider */
    .sidebar-divider {
        border-top: 1px solid #e5e7eb;
        margin-top: 25px;
        margin-bottom: 20px;
    }

    /* login + register row */
    .login-register-row {
        display: flex;
        gap: 10px;
    }

    /* login button */
    .login-button {
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

    /* register button */
    .register-button {
        color: white;
        background-color: #2563eb;
        padding: 14px 18px;
        border-radius: 12px;
        font-size: 16px;
        font-weight: 600;
        width: 48%;
        text-align: center;
    }

    /* page title */
    .page-title {
        font-size: 38px;
        font-weight: 700;
        color: #111827;
        margin-bottom: 2px;
    }

    /* page subtitle */
    .page-subtitle {
        font-size: 20px;
        color: #4b5563;
        margin-bottom: 40px;
    }

    /* info card */
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

    /* upload card */
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

    /* hide real upload */
    div[data-testid="stFileUploader"] {
        display: none;
    }

    /* process button */
    .stButton > button {
        background-color: #d1d5db;
        color: white;
        border: none;
        border-radius: 12px;
        padding: 14px;
        font-size: 18px;
        font-weight: 600;
    }

    /* hide invisible sidebar buttons (for navigation clicks) */
    section[data-testid="stSidebar"] .stButton > button {
        height: 0;
        padding: 0;
        border: none;
        background: none;
    }

    </style>
    """