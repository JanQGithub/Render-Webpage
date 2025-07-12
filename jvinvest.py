import streamlit as st
import base64
import os

st.set_page_config(page_title="JV", layout="wide")

logo_path = os.path.abspath("logo.jpeg")
with open(logo_path, "rb") as image_file:
    logo_base64 = base64.b64encode(image_file.read()).decode("utf-8")

st.markdown(f"""
    <style>
        body {{ margin: 0; font-family: "Segoe UI", Tahoma, Geneva, Verdana, sans-serif; }}
        .top-bar {{
            display: flex; justify-content: space-between; align-items: center; /* Space between logo and hamburger */
            background-color: #004080; color: #ffffff;
            padding: 0 clamp(16px, 4vw, 32px); /* Dynamically adjust padding */
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
            box-sizing: border-box; /* Ensure consistent sizing across browsers */
            position: fixed; width: calc(100% - 2 * clamp(16px, 4vw, 32px)); /* Dynamically adjust width */
            height: calc(14.5vw); margin: 0 auto; /* Center the blue bar with auto margins */
            z-index: 1000;
        }}
        .nav-links {{
            display: flex; gap: 2%; flex-wrap: nowrap;
            position: absolute; /* Position the nav-links */
            left: 50%; /* Center horizontally */
            transform: translateX(-50%); /* Adjust for centering */
        }}
        .nav-links a, .nav-links-mobile a {{
            color: #ffffff; text-decoration: none; font-size: calc(1rem + 0.5vw); font-weight: 500;
            padding: calc(8px + 0.5vw) calc(16px + 0.5vw);
            border-radius: 8px; /* Make corners slightly rounder */
            white-space: nowrap;
            transition: background-color 0.3s ease, color 0.3s ease;
        }}
        .nav-links a:hover, .nav-links a:focus {{
            background-color: #ffcc00; color: #004080;
        }}
        .logo {{
            margin-left: clamp(16px, 4vw, 32px); /* Dynamically adjust margin from the left */
            height: calc(90%); /* Maintain proportional height */
            max-height: calc(14.5vw); /* Dynamically adjust height proportionally */
            min-height: 50px; /* Maintain a minimum height */
        }}
        .logo img {{
            height: 100%; width: auto; /* Maintain aspect ratio */
            transition: height 0.3s ease;
        }}
        .hamburger {{
            display: none; flex-direction: column; cursor: pointer;
            margin-right: clamp(16px, 4vw, 32px); /* Dynamically adjust margin from the right */
            top: 50%; transform: translateY(-50%);
        }}
        .hamburger div {{
            background-color: #ffffff; height: 3px; width: 25px; margin: 4px 0;
        }}
        .nav-links-mobile {{
            display: none; flex-direction: column; background-color: #004080; position: absolute;
            top: calc(14.5vw); /* Adjust top to match new bar height */
            width: 100%; padding: 16px; z-index: 999;
        }}
        .nav-links-mobile a:hover {{
            background-color: #ffcc00; color: #004080;
        }}
        .show {{
            display: flex !important;
        }}
        @media (max-width: 1024px) {{ /* Adjust for smaller screens */
            .top-bar {{
                padding: 0 clamp(16px, 4vw, 32px); /* Dynamically adjust padding */
                width: calc(100% - 2 * clamp(16px, 4vw, 32px)); /* Dynamically adjust width */
                height: calc(20vw); /* Adjust height */
                box-sizing: border-box; /* Ensure consistent sizing */
            }}
            .nav-links {{ display: none; }}
            .hamburger {{ display: flex; }} /* Ensure hamburger is visible */
            .logo {{
                margin-left: clamp(16px, 4vw, 32px); /* Dynamically adjust margin from the left */
                height: calc(90%); /* Maintain proportional height */
                max-height: calc(20vw); /* Dynamically adjust height proportionally */
                min-height: 50px; /* Maintain a minimum height */
            }}
            .logo img {{
                height: 100%; max-height: calc(80%); /* Ensure the logo stays within the blue area */
            }}
            .hamburger {{
                margin-right: clamp(16px, 4vw, 32px); /* Dynamically adjust margin from the right */
            }}
            .nav-links-mobile {{
                top: calc(20vw); /* Adjust top to match new bar height */
            }}
            .content {{
                margin-top: calc(20vw + 20px); /* Adjust margin to match new bar height */
            }}
        }}
        @media (max-width: 900px) {{ /* Adjust breakpoint to show hamburger sooner */
            .top-bar {{
                padding: calc(3vw) calc(6vw); /* Increase padding by 20% */
                width: calc(100% - 2 * calc(3vw)); /* Dynamically adjust width */
                height: calc(17.4vw); /* Increase height by 20% */
            }}
            .nav-links {{ display: none; }}
            .hamburger {{ display: flex; }} /* Ensure hamburger is visible */
            .logo {{
                margin-left: calc(3vw); /* Dynamically adjust margin from the left */
                height: calc(90%); /* Maintain proportional height */
                max-height: calc(20vw); /* Dynamically adjust height proportionally */
                min-height: 50px; /* Maintain a minimum height */
            }}
            .logo img {{
                height: 100%; max-height: calc(96%); /* Ensure the logo stays within the blue area */
            }}
            .hamburger {{
                margin-right: calc(3vw); /* Dynamically adjust margin from the right */
            }}
            .nav-links-mobile {{
                top: calc(17.4vw); /* Adjust top to match new bar height */
            }}
            .content {{
                margin-top: calc(17.4vw + 20px); /* Adjust margin to match new bar height */
            }}
        }}
        @media (max-width: 768px) {{ /* Adjust styles for smaller screens */
            .top-bar {{
                padding: 0 clamp(16px, 4vw, 32px); /* Dynamically adjust padding */
                width: calc(100% - 2 * clamp(16px, 4vw, 32px)); /* Dynamically adjust width */
                height: calc(24vw); /* Adjust height */
                box-sizing: border-box; /* Ensure consistent sizing */
            }}
            .logo {{
                margin-left: clamp(16px, 4vw, 32px); /* Dynamically adjust margin from the left */
                height: calc(90%); /* Maintain proportional height */
                max-height: calc(24vw); /* Dynamically adjust height proportionally */
                min-height: 50px; /* Maintain a minimum height */
            }}
            .logo img {{
                height: 100%; max-height: calc(120%); /* Ensure the logo stays within the blue area */
            }}
            .hamburger {{
                margin-right: clamp(16px, 4vw, 32px); /* Dynamically adjust margin from the right */
            }}
            .nav-links-mobile {{
                top: calc(24vw); /* Adjust top to match new bar height */
            }}
            .content {{
                margin-top: calc(24vw + 20px); /* Adjust margin to match new bar height */
            }}
        }}
        .content {{
            margin-top: calc(14.5vw + 20px); /* Adjust margin to match new bar height */
            padding: 16px;
        }}
    </style>

    <div class="top-bar">
        <div class="logo"><img src="data:image/jpeg;base64,{logo_base64}"></div>
        <div class="hamburger" onclick="document.getElementById('mobile-menu').classList.toggle('show')">
            <div></div><div></div><div></div>
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
        document.querySelector('.hamburger').addEventListener('click', () => {{
            document.getElementById('mobile-menu').classList.toggle('show');
        }});
    </script>
""", unsafe_allow_html=True)

st.write("")
