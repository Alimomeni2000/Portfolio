import streamlit as st
from pathlib import Path
from PIL import Image
import json
from streamlit_lottie import st_lottie
from PIL import Image
import streamlit as st
import base64
from io import BytesIO
import streamlit as st
from streamlit_lottie import st_lottie
import json

list_socialmedia_animation = {
    'linkedin': 'https://www.linkedin.com/in/ali-momeni-b490bb206/',
    'github': 'https://github.com/Alimomeni2000/',
    'telegram': 'https://t.me/alimomeni00',
    'instagram': 'https://www.instagram.com/alimomeni9979',
}

def load_lottie_json(filepath):
    with open(filepath) as f:
        return json.load(f)

# Create columns for each social media platform
cols = st.columns(len(list_socialmedia_animation))
for col, (platform, url) in zip(cols, list_socialmedia_animation.items()):
    lottie_animation = load_lottie_json(f'./assets/{platform}.json')
    with col:
        click_placeholder = st.empty()
        with click_placeholder:
            # Display Lottie animation
            st_lottie(lottie_animation, width=100, height=100, key=platform)  
            
            # Add CSS to make the background transparent
            st.markdown(
                """
                <style>
                .css-1aumxhk {
                    background-color: rgba(255, 255, 255, 0);
                }
                </style>
                """,
                unsafe_allow_html=True
            )

        st.markdown(f'<a href="{url}" target="_blank" style="position:relative; top:-120px; display:block; width:100px; height:100px;"></a>', unsafe_allow_html=True)
