import streamlit as st
import base64
import os

# --- Page config ---
st.set_page_config(
    page_title="JV Invest",
    page_icon="🍔",
    layout="wide"
)

# --- Encode the logo image in base64 ---
logo_path = os.path.abspath("logo.jpeg")
with open(logo_path, "rb") as image_file:
    logo_base64 = base64.b64encode(image_file.read()).decode("utf-8")

# --- Hamburger-style Top Bar ---
st.markdown(f"""
    <style>
        body {{
            margin: 0;
            font-family: "Segoe UI", Tahoma, Geneva, Verdana, sans-serif;
        }}
        .top-bar {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            background-color: #004080; /* Adjusted to match logo */
            color: #ffffff;
            padding: 12px 32px;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
            position: relative;
        }}
        .logo img {{
            width: 120px;
            transition: width 0.3s ease;
        }}
        .hamburger {{
            display: none;
            flex-direction: column;
            cursor: pointer;
        }}
        .hamburger div {{
            background-color: #ffffff;
            height: 3px;
            width: 25px;
            margin: 4px 0;
            transition: all 0.6s ease;
        }}
        .nav-links {{
            display: flex;
            gap: 24px;
        }}
        .nav-links a {{
            color: #ffffff;
            text-decoration: none;
            font-size: 1rem;
            font-weight: 500;
            transition: color 0.3s ease, font-size 0.3s ease;
        }}
        .nav-links a:hover {{
            color: #ffcc00; /* Accent color */
        }}
        .nav-links-mobile {{
            display: none;
            flex-direction: column;
            background-color: #004080; /* Adjusted to match logo */
            position: absolute;
            top: 60px;
            right: 32px;
            padding: 16px;
            border-radius: 8px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
            z-index: 1000;
        }}
        .nav-links-mobile a {{
            color: #ffffff;
            text-decoration: none;
            font-size: 1rem;
            font-weight: 500;
            padding: 8px 0;
            transition: color 0.3s ease;
        }}
        .nav-links-mobile a:hover {{
            color: #ffcc00; /* Accent color */
        }}
        .show {{
            display: flex !important;
        }}
        @media (max-width: 768px) {{
            .nav-links {{
                display: none;
            }}
            .hamburger {{
                display: flex;
            }}
        }}
        @media (min-width: 1024px) {{
            .logo img {{
                width: 160px; /* Increase logo size for larger screens */
            }}
            .nav-links a {{
                font-size: 1.4rem; /* Increase font size for larger screens */
            }}
        }}
        @media (min-width: 1440px) {{
            .logo img {{
                width: 200px; /* Further increase logo size for very large screens */
            }}
            .nav-links a {{
                font-size: 1.8rem; /* Further increase font size for very large screens */
            }}
        }}
        @media (min-width: 1920px) {{
            .logo img {{
                width: 240px; /* Maximum logo size for ultra-wide screens */
            }}
            .nav-links a {{
                font-size: 2.2rem; /* Maximum font size for ultra-wide screens */
            }}
        }}
    </style>
    <div class="top-bar">
        <div class="logo">
            <img src="data:image/jpeg;base64,{logo_base64}">
        </div>
        <div class="hamburger" onclick="document.getElementById('mobile-menu').classList.toggle('show')">
            <div></div>
            <div></div>
            <div></div>
        </div>
        <div class="nav-links">
            <a href="#about">About</a>
            <a href="#services">Services</a>
            <a href="#portfolio">Portfolio</a>
            <a href="#contact">Contact</a>
        </div>
        <div class="nav-links-mobile" id="mobile-menu">
            <a href="#about">About</a>
            <a href="#services">Services</a>
            <a href="#portfolio">Portfolio</a>
            <a href="#contact">Contact</a>
        </div>
    </div>
    <script>
        document.addEventListener('DOMContentLoaded', function() {{
            const hamburger = document.querySelector('.hamburger');
            const mobileMenu = document.getElementById('mobile-menu');
            hamburger.addEventListener('click', function() {{
                mobileMenu.classList.toggle('show');
            }});
        }});
    </script>
""", unsafe_allow_html=True)

# --- Content ---
st.markdown("### Content will be shown soon!")
st.write("")
