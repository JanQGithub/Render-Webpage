import streamlit as st
import base64
import os

# --- Page config ---
st.set_page_config(
    page_title="JV",
    layout="wide"
)

# --- Encode the logo image in base64 ---
logo_path = os.path.abspath("logo.jpeg")
with open(logo_path, "rb") as image_file:
    logo_base64 = base64.b64encode(image_file.read()).decode("utf-8")

# --- Top Bar ---
st.markdown(f"""
    <style>
        body {{
            margin: 0;
            font-family: "Segoe UI", Tahoma, Geneva, Verdana, sans-serif;
        }}
        .top-bar {{
            display: flex;
            justify-content: center; /* Center align the links */
            align-items: center;
            background-color: #004080; /* Adjusted to match logo */
            color: #ffffff;
            padding: calc(2vw) calc(4vw); /* Dynamically adjust padding */
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
            position: fixed; /* Keep the top bar fixed */
            height: calc(12vw); /* Dynamically adjust height */
            width: 100%;
            z-index: 1000;
        }}
        .nav-links {{
            display: flex;
            gap: 2%; /* Adjust gap dynamically */
            flex-wrap: nowrap; /* Prevent wrapping of links */
        }}
        .nav-links a {{
            color: #ffffff;
            text-decoration: none;
            font-size: calc(1.2rem + 1vw); /* Dynamically increase font size */
            font-weight: 500;
            text-align: center;
            padding: calc(8px + 0.5vw) calc(16px + 0.5vw); /* Dynamically adjust padding */
            border-radius: 4px;
            transition: background-color 0.3s ease, color 0.3s ease, font-size 0.3s ease;
            white-space: nowrap; /* Prevent text wrapping */
        }}
        .nav-links a:hover, .nav-links a:focus {{
            background-color: #ffcc00; /* Highlight color */
            color: #004080; /* Text color on highlight */
        }}
        .logo {{
            position: absolute;
            left: calc(2vw); /* Dynamically position logo */
            height: calc(90%); /* Ensure the logo stays smaller than the blue area */
        }}
        .logo img {{
            height: 100%; /* Adjust logo size automatically */
            max-height: calc(12vw); /* Ensure the logo stays within the blue area */
            transition: height 0.3s ease;
        }}
        .hamburger {{
            display: none;
            flex-direction: column;
            cursor: pointer;
            position: absolute;
            right: calc(4vw); /* Move hamburger slightly more toward the middle */
            top: 50%; /* Center vertically in the blue bar */
            transform: translateY(-50%); /* Adjust for perfect centering */
        }}
        .hamburger div {{
            background-color: #ffffff;
            height: 3px;
            width: 25px;
            margin: 4px 0;
            transition: all 0.3s ease;
        }}
        .nav-links-mobile {{
            display: none;
            flex-direction: column;
            background-color: #004080; /* Match top bar color */
            position: absolute;
            top: calc(12vw); /* Position below the top bar */
            width: 100%;
            padding: 16px;
            z-index: 999;
        }}
        .nav-links-mobile a {{
            color: #ffffff;
            text-decoration: none;
            font-size: calc(1rem + 0.5vw); /* Dynamically increase font size */
            padding: 8px 16px;
            border-radius: 4px;
            transition: background-color 0.3s ease, color 0.3s ease;
        }}
        .nav-links-mobile a:hover {{
            background-color: #ffcc00; /* Highlight color */
            color: #004080; /* Text color on highlight */
        }}
        .show {{
            display: flex !important; /* Show mobile menu */
        }}
        @media (max-width: 768px) {{
            .nav-links {{
                display: none; /* Hide links on mobile */
            }}
            .hamburger {{
                display: flex; /* Show hamburger menu on mobile */
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
            <a href="#Education">Education</a>
            <a href="#News">News</a>
            <a href="#Links">Links</a>
            <a href="#Contact">Contact</a>
        </div>
    </div>
    <div class="nav-links-mobile" id="mobile-menu">
        <a href="#Education">Education</a>
        <a href="#News">News</a>
        <a href="#Links">Links</a>
        <a href="#Contact">Contact</a>
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
