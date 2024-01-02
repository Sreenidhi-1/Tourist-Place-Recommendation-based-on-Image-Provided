import streamlit as st
import os
l = os.listdir(r"plots")
st.write("<h1 style='text-align: center;color:  #FFA500;'>PLOTS</h1><br><br>", unsafe_allow_html=True)

root = "plots"
page_bg_img = f"""
    <style>
    [data-testid="stAppViewContainer"] > .main {{
        
        background-size: 200% 200%;
        animation: radialGradientAnimation 10s infinite linear;
    }}
        [data-testid="stSidebar"] {{
    
        background-size: cover;
        background-position: top left;
        background-attachment: local;
    }}
    
    [data-testid="stToolbar"] {{
        right: 2rem;
    }}

    @keyframes radialGradientAnimation {{
        0% {{
            background-position: 0% 0%;
        }}
        100% {{
            background-position: 100% 100%;
        }}
    }}

    @keyframes linearGradientAnimation {{
        0% {{
            background-position: 0% 0%;
        }}
        100% {{
            background-position: 100% 100%;
        }}
    }}
    </style>
"""

st.markdown(page_bg_img, unsafe_allow_html=True)
for i in l:
    first_image_path = os.path.join(root, i)
    st.subheader(i.split(".")[0])
    st.image(first_image_path)
