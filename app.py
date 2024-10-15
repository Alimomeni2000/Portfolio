import streamlit as st
from pathlib import Path
from PIL import Image
import json
from streamlit_lottie import st_lottie
from PIL import Image
import streamlit as st
import base64
from io import BytesIO


page_bg_img = """
<style>
[data-testid="stAppViewContainer"]{
background-color: #181b33;
opacity: 1;
background-image:  linear-gradient(30deg, #150d2f 12%, transparent 12.5%, transparent 87%, #150d2f 87.5%, #150d2f), linear-gradient(150deg, #150d2f 12%, transparent 12.5%, transparent 87%, #150d2f 87.5%, #150d2f), linear-gradient(30deg, #150d2f 12%, transparent 12.5%, transparent 87%, #150d2f 87.5%, #150d2f), linear-gradient(150deg, #150d2f 12%, transparent 12.5%, transparent 87%, #150d2f 87.5%, #150d2f), linear-gradient(60deg, #150d2f77 25%, transparent 25.5%, transparent 75%, #150d2f77 75%, #150d2f77), linear-gradient(60deg, #150d2f77 25%, transparent 25.5%, transparent 75%, #150d2f77 75%, #150d2f77);
background-size: 80px 80px;
background-position: 0 0, 0 0, 17px 30px, 17px 30px, 0 0, 17px 30px;
"""
st.markdown(page_bg_img, unsafe_allow_html=True)

def txt(a, b, num):
    col1, col2 = st.columns(num)
    with col1:
        st.markdown(a)
    with col2:
        st.markdown(b)


current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV.pdf"
profile_pic_path = current_dir / "assets" / "profile-pic.png"
lottie_file_path = current_dir / "assets" / "Animation - 1728851770914.json"

def load_lottie_json(filepath: str):
    with open(filepath) as f:
        return json.load(f)

PAGE_TITLE = "Digital CV | Ali Momeni"
PAGE_ICON = ":wave:"
NAME = "Ali Momeni"
DESCRIPTION = "As a computer engineering graduate from Shahid Chamran University of Ahvaz, I have focused on applying deep learning and AI to healthcare challenges, particularly in medical image analysis. Throughout my studies, I’ve worked on projects like classifying epilepsy and plant disease images using neural networks, and developing AI-driven robotic systems. I’m passionate about leveraging technology to solve real-world problems, especially in the field of healthcare."
EMAIL = "alimomeni2000.official@email.com"

st.markdown("""
    <div class="navbar">
        <ul>
            <li><a href="#about">About</a></li>
            <li><a href="#education">Education</a></li>
            <li><a href="#research_interests">Research Interests</a></li>
            <li><a href="#skills">Skills</a></li>
            <li><a href="#certifications">Certifications</a></li>
            <li><a href="#projects">Projects</a></li>
            <li><a href="#references">References</a></li>
            <li><a href="#contact">Contact</a></li>
        </ul>
    </div>
""", unsafe_allow_html=True)

with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)

with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()

profile_pic = Image.open(profile_pic_path)

st.markdown("<div id='about'></div>", unsafe_allow_html=True)
st.title("About Me")

# lottie_animation = load_lottie_json(lottie_file_path)

# st_lottie(lottie_animation)
col1, col2 = st.columns(2, gap="small")
with col1:
    
    st.image(profile_pic, width=380)
with col2:
    st.title(NAME)
    st.info(DESCRIPTION)

    st.download_button(
        label="📄 Download Resume",
        data=PDFbyte,
        file_name="Ali_Momeni_Resume.pdf",
        mime="application/octet-stream",
    )

   
    # Function to convert image to base64
    def img_to_base64(image: Image.Image) -> str:
        buffered = BytesIO()
        image.save(buffered, format="PNG")
        img_str = base64.b64encode(buffered.getvalue()).decode("utf-8")
        return img_str

    # Load your image
    profile_pic = Image.open("./assets/gmail.png")

    # Convert the image to base64
    image_base64 = img_to_base64(profile_pic)

    # Create the HTML string for the image
    image_html = f'<img src="data:image/png;base64,{image_base64}" width="60" height="50" style="border-radius: 25%;">'

    # Combine image and text
    combined_html = f"""
        <div style="display: flex; align-items: center;">
            {image_html}
            <a href="{EMAIL}"><span style="font-size: 20px;margin-left: 15px;">alimomeni2000.official@gmail.com</span></a>
            
        </div>
    """
    # Display in Streamlit
    st.markdown(combined_html, unsafe_allow_html=True)

st.markdown('<hr style="height:2px;border:none;color:#f2f3f4;background-color:#f2f3f4;" />',  unsafe_allow_html=True )

st.markdown("<div id='education'></div>", unsafe_allow_html=True)
st.title("Education")
st.write('\n')
txt(f"""##### *B.Sc Computer Engineering*, *[Shahid Chamran University of Ahvaz](URL)*""", "**Ahvaz-Iran 2019-2023**",[6,2.25])
st.markdown(''' 
   ###### - **GPA**: 16.08/20 (3.35/4)
   ###### - **Thesis**: Classification of medical images of epilepsy patients using deep neural networks
   ###### - **CGPA of the last two semesters**: 17.70/20 (3.68/4)
   ###### - **CGPA of Specialized Courses**: 17.60/20 (3.63/4)
   ###### - **Thesis grade**: 4/4
   ###### - **Advisors**: **[Dr. Ali Bakhthamat](URL)**, **[Dr. Seyed Enayatallah Alavi](URL)**
''')


txt("""##### *Mathematics and Physics Diploma*, *Allameh Tabatabaei High School*""", "**Aleshtar 2019**",[6,2.5])
st.markdown('''
    ###### - **GPA**: *18.21*/20 (*3.76*/4)
''')
st.markdown('<hr style="height:2px;border:none;color:#f2f3f4;background-color:#f2f3f4;" />',  unsafe_allow_html=True )
st.markdown("<div id='research_interests'></div>", unsafe_allow_html=True)
st.title("Research Interests")
st.markdown(''' 
##### - Computer vision based healthcare system
##### - Robotic Technologies in Pharmacy and Medicine
##### - Human-Computer Interaction
##### - Machine learning and deep learning approach for medical image analysis
##### - Remote patient monitoring
#####  - 3D Medical image Reconstruction and Visualization
''')


st.markdown('<hr style="height:2px;border:none;color:#f2f3f4;background-color:#f2f3f4;" />',  unsafe_allow_html=True )
st.markdown("<div id='Skills'></div>", unsafe_allow_html=True)
st.title("Skills")
txt('##### **Programming**', '##### `Python`, `C/C++`, `Java`, `R(basic)`, `VHDL/Verilog`', [1, 2])  
txt('##### Data processing', '##### `SQL`, `pandas`, `numpy`', [1, 2])  
txt('##### Machine Learning', '##### `scikit-learn`', [1, 2])  
txt('##### Deep Learning', '##### `TensorFlow`, `Keras`', [1, 2])  
txt('##### Web development', '##### `Django`, `FastAPI`, `HTML`, `CSS`', [1, 2])  
txt('##### Model deployment', '##### `streamlit`', [1, 2])  
txt('##### Software Skills', '##### `Google Colab`, `MySQL`, `PostgreSQL`, `Git/Github`, `Visual Paradigm`, `Xilinx ISE`, `Webots`, `LATEX`, `Excel`, `Bash`', [1, 2])  
txt('##### OS', '##### `Linux`, `Windows`', [1, 2])  

st.markdown('<hr style="height:2px;border:none;color:#f2f3f4;background-color:#f2f3f4;" />',  unsafe_allow_html=True )
st.markdown("<div id='certifications'></div>", unsafe_allow_html=True)
st.title("Certifications")

txt('''##### **[Advanced Learning Algorithms](https://www.coursera.org/account/accomplishments/verify/3TU4CH69L2SQ)** \n - Build and train a neural network with TensorFlow to perform multi-class classification
    \n - Build and use decision trees and tree ensemble methods, including random forests and boosted trees
''', '###### Coursera Feb 2024', [3, 1])  

st.markdown('<hr style="border: none; border-top: 1px dotted #d6dbdf; margin: 20px 0;" />',  unsafe_allow_html=True )

txt('''##### **[Supervised Machine Learning: Regression and Classification](https://www.coursera.org/account/accomplishments/verify/GD5S7QU3S8ZP)** \n - Build machine learning models in Python using popular machine learning libraries NumPy & scikit-learn \n
- Build & train supervised machine learning models for prediction & binary classification tasks, including linear regression & logistic regression
''', '###### Coursera Feb 2024', [3, 1])  


st.markdown('<hr style="height:2px;border:none;color:#f2f3f4;background-color:#f2f3f4;" />',  unsafe_allow_html=True )
st.markdown("<div id='projects'></div>", unsafe_allow_html=True)
st.title("Projects")

st.markdown('<hr style="height:2px;border:none;color:#f2f3f4;background-color:#f2f3f4;" />',  unsafe_allow_html=True )
st.markdown("<div id='references'></div>", unsafe_allow_html=True)
st.title("References")
st.markdown(''' 
    ##### - **Name:** <u>Dr. Seyed Enayatallah Alavi</u>
    ##### - **Email:** se.alavi@scu.ac.ir
    ###### - **Assistant professor in Shahid Chamran University of Ahvaz**
    ###### **Bachelor’s project supervisor**
    <hr style="border: none; border-top: 1px dotted #d6dbdf; margin: 20px 0;" />

    ##### - **Name:** <u>Elham Nikookar</u>
    ##### - **Email:** e.nikookar@scu.ac.ir / nikookar.cse@gmail.com
    ###### **Lecturer in Shahid Chamran University of Ahvaz**

    <hr style="border: none; border-top: 1px dotted #d6dbdf; margin: 20px 0;" />
    
    ##### - **Name:** <u>Dr. Ali Bakhthemat</u>
    ##### - **Email:** bakhthemmat.std@gmail.com
    ###### **Lecturer in Shahid Chamran University of Ahvaz**
    ###### **Bachelor’s project supervisor**

''', 
    unsafe_allow_html=True)

st.markdown('<hr style="height:2px;border:none;color:#f2f3f4;background-color:#f2f3f4;" />',  unsafe_allow_html=True )
st.markdown("<div id='contact'></div>", unsafe_allow_html=True)
st.title("Contact")

list_socialmedia_animation = {
    'linkedin': 'https://www.linkedin.com/in/ali-momeni-b490bb206/',
    'github': 'https://github.com/Alimomeni2000/',
    'telegram': 'https://t.me/alimomeni00',
    'instagram': 'https://www.instagram.com/alimomeni9979',
}

# Load the Lottie animation
lottie_animation = load_lottie_json('./assets/linkedin.json')

cols = st.columns(len(list_socialmedia_animation))
for col, (platform, url) in zip(cols, list_socialmedia_animation.items()):
    lottie_animation = load_lottie_json(f'./assets/{platform}.json')
    with col:
        click_placeholder = st.empty()
        with click_placeholder:
            st_lottie(lottie_animation, width=100, height=100)
        st.markdown(f'<a href="{url}" target="_blank" style="background-color= transparent !important;position:relative; top:120px; display:block; width:100px; height:100px;"></a>', unsafe_allow_html=True)

col1, col2 = st.columns([2, 1])
lottie_animation = load_lottie_json('./assets/Animation - 1728895738988.json')
with col2:
    st_lottie(lottie_animation, width=350, height=350)

with col1:
    contact_form = """
<form action="https://formsubmit.co/alimomeni2000.official@gmail.com" method="POST">
    <input type="text" name="name" placeholder="Your Name" required>
    <input type="email" name="email" placeholder="Your Email" required>
    <textarea name="message" placeholder="Your Message" rows="4" required></textarea>
    <button type="submit">Send</button>
</form>
    """
    st.markdown(contact_form, unsafe_allow_html=True)

