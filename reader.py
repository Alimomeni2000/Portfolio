import streamlit as st
import json

# --- PAGE CONFIGURATIONS ---
PAGE_TITLE = "Digital CV | Ali Momeni"
PAGE_ICON = ":wave:"
st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

# --- PERSONAL INFORMATION ---
NAME = "Ali Momeni"
DESCRIPTION = ("As a computer engineering graduate from Shahid Chamran University of Ahvaz, "
               "I have focused on applying deep learning and AI to healthcare challenges, "
               "particularly in medical image analysis. Throughout my studies, I’ve worked "
               "on projects like classifying epilepsy and plant disease images using neural "
               "networks, and developing AI-driven robotic systems. I’m passionate about "
               "leveraging technology to solve real-world problems, especially in healthcare.")
EMAIL = "alimomeni2000.official@email.com"

# --- URLs ---
EDUCATION_URLS = {
    "Shahid Chamran University of Ahvaz": "https://scu.ac.ir/en/%D8%B5%D9%81%D8%AD%D9%87-%D8%A7%D8%B5%D9%84%DB%8C",
    "Dr. Ali Bakhthamat": "https://scholar.google.com/citations?user=7bewisgAAAAJ&hl=en&oi=ao",
    "Dr. Seyed Enayatallah Alavi": "https://scholar.google.com/citations?user=-xRyl_IAAAAJ&hl=en",
}

# --- NAVBAR ---
navbar = """
    <div class="navbar">
        <a href="#about" class="active">About</a>
        <a href="#education">Education</a>
        <a href="#research_interests">Research Interests</a>
        <a href="#skills">Skills</a>
        <a href="#certifications">Certifications</a>
        <a href="#projects">Projects</a>
        <a href="#references">References</a>
        <a href="#contact">Contact</a>
    </div>
"""
st.markdown(navbar, unsafe_allow_html=True)

# --- FUNCTIONS ---
def txt(a, b, num):
    col1, col2 = st.columns(num)
    with col1:
        st.markdown(a)
    with col2:
        st.markdown(b)

def load_lottie_json(filepath: str):
    with open(filepath) as f:
        return json.load(f)

# --- EDUCATION SECTION ---
uni_place = [
    "##### *B.Sc Computer Engineering*, *[Shahid Chamran University of Ahvaz](URL)*",
    "**Ahvaz-Iran 2019-2023**"
]

uni_education = ''' 
   ###### - **GPA**: 16.08/20 (3.35/4)
   ###### - **Thesis**: Classification of medical images of epilepsy patients using deep neural networks
   ###### - **CGPA of the last two semesters**: 17.70/20 (3.68/4)
   ###### - **CGPA of Specialized Courses**: 17.60/20 (3.63/4)
   ###### - **Thesis grade**: 4/4
   ###### - **Advisors**: **[Dr. Ali Bakhthamat](URL)**, **[Dr. Seyed Enayatallah Alavi](URL)**
'''

# High School Section
high_place = [
    "##### *Mathematics and Physics Diploma*, *Allameh Tabatabaei High School*",
    "**Aleshtar 2019**"
]

high_education = '''
    ###### - **GPA**: *18.21*/20 (*3.76*/4)
'''

# --- RESEARCH INTERESTS ---
research_interests = ''' 
##### - Computer vision-based healthcare systems
##### - Robotic technologies in pharmacy and medicine
##### - Human-Computer Interaction
##### - Machine learning and deep learning approaches for medical image analysis
##### - Remote patient monitoring
##### - 3D medical image reconstruction and visualization
'''

# --- EXPERIENCE ---
experiences_academic = [
    ['''#### **Teaching Assistant for Software Engineering** 
    \n - Prepared and presented lectures and recitations, supported term projects, helped students with course materials, and graded homework 
    ''', '###### Ahvaz-Iran, Jan-Jul 2023'],
    
    ['''#### **Teaching Assistant for Fundamentals of Programming** 
    \n - Managed the teaching assistants team, prepared and presented lectures and recitations, supported term projects.
    ''', '###### Ahvaz-Iran, Jan-Jul 2022'],

    ['''#### **Teaching Assistant for Advanced Programming** 
    \n - Prepared and presented lectures and recitations, supported term projects, helped students with course materials, and graded homework.
    ''', '###### Ahvaz-Iran, Sep-Dec 2021'],
]

experiences_professional = [
    ['''#### **‌Behbod Gostar Andishe - `Part-time`** 
    \n - Implemented machine learning algorithms and image processing techniques.
    ''', '###### Ahvaz-Iran, Nov 2022 - Dec 2023'],
]

# --- SKILLS ---
skills_list = [
    ['##### **Programming**', '##### `Python`, `C/C++`, `Java`, `R (basic)`, `VHDL/Verilog`'],
    ['##### **Data Processing**', '##### `SQL`, `pandas`, `numpy`'],
    ['##### **Machine Learning**', '##### `scikit-learn`'],
    ['##### **Deep Learning**', '##### `TensorFlow`, `Keras`'],
    ['##### **Web Development**', '##### `Django`, `FastAPI`, `HTML`, `CSS`'],
    ['##### **Model Deployment**', '##### `streamlit`'],
    ['##### **Software Skills**', '##### `Google Colab`, `MySQL`, `PostgreSQL`, `Git/Github`, `Xilinx ISE`, `Webots`, `LATEX`, `Excel`, `Bash`'],
    ['##### **Operating Systems**', '##### `Linux`, `Windows`'],
]

# --- SKILLS ---
professional_projects = [
    # ['##### **[Analysis of electricity consumption by subscribers of Behbahan city, Iran(Sreamlit app)](https://github.com/Alimomeni2000/Electricity_consumption_system_subscribers_Behbahan)**',

    ['##### **[Chest X-ray Pneumonia Classification](https://github.com/Alimomeni2000/XrayChest)** \n - ##### a deep learning project was conducted to classify chest X-ray images to identify associated diseases accurately.' ,
      '###### sklearn, streamlit, plotly, pandas,catboost,xgboost, numpy, seaborn', "https://raw.githubusercontent.com/Alimomeni2000/XrayChest/main/XrayChest.ipynb"],
    #   '###### streamlit, plotly, pandas, numpy, seaborn'],
    ['##### **[Chest X-ray Pneumonia Classification](https://github.com/Alimomeni2000/XrayChest)** \n - ##### a deep learning project was conducted to classify chest X-ray images to identify associated diseases accurately.' ,
      '###### sklearn, streamlit, plotly, pandas,catboost,xgboost, numpy, seaborn', "https://raw.githubusercontent.com/Alimomeni2000/Black-Friday-Sale/main/Black%20Friday%20Sale.ipynb"],


]

# --- CERTIFICATIONS ---
certifications = [
    ['''##### **[Advanced Learning Algorithms](https://www.coursera.org/account/accomplishments/verify/3TU4CH69L2SQ)** 
    \n - Built and trained a neural network with TensorFlow for multi-class classification.
    \n - Developed and utilized decision trees and tree ensemble methods.
    ''', '###### Coursera, Feb 2024'],
    
    ['''####٫ **[Supervised Machine Learning: Regression and Classification](https://www.coursera.org/account/accomplishments/verify/GD5S7QU3S8ZP)** 
    \n - Built machine learning models in Python using NumPy & scikit-learn. 
    \n - Built and trained supervised models for regression and classification tasks.
    ''', '###### Coursera, Feb 2024'],
]

# --- REFERENCES ---
references = ''' 
    - ##### **Name:** <u>Dr. Seyed Enayatallah Alavi</u>
    - ##### **Email:** se.alavi@scu.ac.ir
    - ##### **Position:** Assistant professor, Shahid Chamran University of Ahvaz
    - ##### **Role:** Bachelor's project supervisor
    <hr style="border: none; border-top: 1px dotted #d6dbdf; margin: 20px 0;" />

    - ##### **Name:** <u>Elham Nikookar</u>
    - ##### **Email:** e.nikookar@scu.ac.ir / nikookar.cse@gmail.com
    - ##### **Position:** Lecturer, Shahid Chamran University of Ahvaz
    <hr style="border: none; border-top: 1px dotted #d6dbdf; margin: 20px 0;" />
    
    - ##### **Name:** <u>Dr. Ali Bakhthemat</u>
    - ##### **Email:** bakhthemmat.std@gmail.com
    - ##### **Position:** Lecturer, Shahid Chamran University of Ahvaz
    - ##### **Role:** Bachelor's project supervisor
'''

# --- PROJECTS ---
PROJECTS = {  
    "🏆 Sales Dashboard - Comparing sales across three stores": "https://youtu.be/Sb0A9i6d320",  
    "🏆 Income and Expense Tracker - Web app with NoSQL database": "https://youtu.be/3egaMfE9388",  
    "🏆 Desktop Application - Excel2CSV converter with user settings & menubar": "https://youtu.be/LzCfNanQ_9c",  
    "🏆 MyToolBelt - Custom MS Excel add-in to combine Python & Excel": "https://pythonandvba.com/mytoolbelt/",  
}  

# --- CONTACT FORM ---
contact_form = """
<form action="https://formsubmit.co/alimomeni2000.official@gmail.com" method="POST">
    <input type="text" name="name" placeholder="Your Name" required>
    <input type="email" name="email" placeholder="Your Email" required>
    <textarea name="message" placeholder="Your Message" rows="4" required></textarea>
    <button type="submit">Send</button>
</form>
"""
st.markdown(contact_form, unsafe_allow_html=True)
