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

    </style>
    """