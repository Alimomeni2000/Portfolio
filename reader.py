import streamlit as st
import json

# --- PAGE CONFIGURATIONS ---
PAGE_TITLE = "Digital CV | Ali Momeni"
PAGE_ICON = ":wave:"

# --- PERSONAL INFORMATION ---
NAME = "Ali Momeni"
DESCRIPTION = ("- As a computer engineering graduate from Shahid Chamran University of Ahvaz, "
               "\n- I have focused on applying deep learning and AI to healthcare challenges, "
               "\n- particularly in medical image analysis. Throughout my studies, I’ve worked "
               "on projects like classifying epilepsy and plant disease images using neural "
               "networks, and developing AI-driven robotic systems. \n- I’m passionate about "
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
 ['##### **[Chest X-ray Pneumonia Classification](https://github.com/Alimomeni2000/Electricity_consumption_system_subscribers_Behbahan)** \n - ##### In the electricity consumption analysis project, subscribers of a city, multiple electricity consumption patterns were investigated by plotly, seaborn, Matplotlib, and its web application was designed by streamlit Lib. By analyzing these patterns, efforts were made to improve productivity and sustainable management of electricity consumption in society.' ,
      '###### sklearn, streamlit, plotly, pandas, numpy, seaborn', 'None'],
    
    ['##### **[Chest X-ray Pneumonia Classification](https://github.com/Alimomeni2000/XrayChest)** \n - ##### a deep learning project was conducted to classify chest X-ray images to identify associated diseases accurately.' ,
      '###### sklearn, streamlit, plotly, pandas,catboost,xgboost, numpy, seaborn', "https://raw.githubusercontent.com/Alimomeni2000/Black-Friday-Sale/main/Black%20Friday%20Sale.ipynb"],
    ['##### **[ISNA_Cronanews](https://github.com/Alimomeni2000/ISNA_Cronanews)** \n - #####  In the deep learning project, the news was categorized to identify different topics and categories accurately. Deep models were used to improve accuracy and efficiency up to **88%** in analyzing and classifying news published by the Iranian Students News Agency.' ,
      '###### sklearn, streamlit, plotly, pandas,catboost,xgboost, numpy, seaborn', "https://raw.githubusercontent.com/Alimomeni2000/ISNA_Cronanews/blob/main/Isna.ipynb"],
   
    ['##### **[Average car Prices - Brazil](https://github.com/Alimomeni2000/Brazil-Car-Prices)** \n - #####  fying news published by the Iranian Students News Agency. Average car Prices - Brazil, With expertise in machine learning regression algorithms, including EDA, Decision Tree Regressor, Random Forest Regressor,..., Catboost and XGBoost, the project improved the R2 score to over 99% through the use of effective data cleaning techniques.' ,
      '###### sklearn, streamlit, plotly, pandas,catboost,xgboost, numpy, seaborn', "https://raw.githubusercontent.com/Alimomeni2000/ISNA_Cronanews/blob/main/Isna.ipynb"],
    
    ['##### **[Fake/True news classification](https://github.com/Alimomeni2000/Fake_True_News)** \n - #####  A Neural Language Model was developed to classify news articles as fake or real, employing machine learning algorithms such as K Neighbors Classifier, Decision Tree Classifier, etc, from the Scikit-learn library. NLTK was integrated for enhanced natural language processing capabilities.' ,
      '###### sklearn, streamlit, plotly, pandas,catboost,xgboost, numpy, seaborn', "https://raw.githubusercontent.com/Alimomeni2000/Fake_True_News/blob/main/Fake_True_News.ipynb"],


]




academic_projcts =  [  
    ['''#### **Classification of medical images of epilepsy patients using deep neural networks**   
    \n - Utilized Pydicom, Scikit-learn, and NumPy for data loading and conversion to numerical arrays. Employed Keras and Tensorflow for the design of CNN models.   
    \n - **Bachelor’s Thesis**, Professors A. Bakhthamat, S.E. Alavi, 2023  
    ''',   
    '###### Ahvaz-Iran, 2023']  ,

    ['''#### **Classification of plant disease images using Transfer Learning (AlexNet)** 
    \n - Implemented with Keras and Tensorflow.
    \n - **Project for the course "Fundamentals of Computer Vision"**, Prof F. Abbasi, 2023
    ''', '###### Ahvaz-Iran, 2023'],

    ['''#### **Robot design capable of executing tasks such as linear and rotational movements, wall following, and search algorithms (A*)** 
    \n - Utilized Python and Webots simulation for the design and implementation of artificial intelligence algorithms.
    \n - **Project for the course "Principles of Robotics"**, Prof A. Ghanbarzadeh, 2023
    ''', '###### Ahvaz-Iran, 2023'],

    ['''#### **Online Warehouse System Design** 
    \n - Designed system models and created UML diagrams (class, use case, sequence, communication, activity) using Visual Paradigm.
    \n - **Project for the course "Software Engineering Lab"**, Prof A. Bakhthemat, 2023
    ''', '###### Ahvaz-Iran, 2023'],

    ['''#### **ARM Single Cycle Microprocessor Circuit** 
    \n - Designed using VHDL in Xilinx ISE.
    \n - **Project for the course "Computer Design of Digital Systems"**, Prof B. Saniei, 2023
    ''', '###### Ahvaz-Iran, 2023'],

    ['''#### **Working on network switches for the educational network of Aleshtar city** 
    \n - Internship project focusing on network infrastructure.
    \n - **Internship Project**, Prof M.J. Rashti, 2022
    ''', '###### Aleshtar-Iran, 2022'],

    ['''#### **Online Bookstore System Design** 
    \n - Designed system models and created UML diagrams (class, use case, sequence, communication, activity) using Visual Paradigm.
    \n - **Project for the course "Software Engineering"**, Prof A. Bakhthamat, 2022
    ''', '###### Ahvaz-Iran, 2022'],

    ['''#### **Implementation of the Eight-Puzzle Game and Sudoku Solver** 
    \n - Utilized UCS, IDS, IDA*, A* search algorithms for the Eight-Puzzle Game and backtracking with MRV and degree heuristics for Sudoku.
    \n - **Project for the course "Artificial Intelligence"**, Prof S. Loveymi, 2022
    ''', '###### Ahvaz-Iran, 2022'],

    ['''#### **Packet Information Extraction Using Scapy** 
    \n - Extracted packet information using Python and Scapy.
    \n - **Project for the course "Computer Networks"**, Prof M. Naderann, 2022
    ''', '###### Ahvaz-Iran, 2022'],

    ['''#### **Design and Implementation of an Online Service Work Order System** 
    \n - Modeled systems using UML diagrams in Visual Paradigm and implemented the system using Django, PostgreSQL, HTML, and CSS.
    \n - **Project for the course "Systems Analysis and Design"**, Prof B. Mayahi, 2021
    ''', '###### Ahvaz-Iran, 2021'],

    ['''#### **Design and Implementation of a Database Management System** 
    \n - Complete planning and creation of database design components (ERD, relational schemas, normalization) using MySQL.
    \n - **Project for the course "Databases"**, Prof S. Zobeidi, 2021
    ''', '###### Ahvaz-Iran, 2021'],

    ['''#### **Romanian Road Algorithm Using Gridsearch and Graph** 
    \n - Implemented using Python.
    \n - **Project for the course "Discrete Mathematics"**, Prof M. Farokhian, 2020
    ''', '###### Ahvaz-Iran, 2020'],
]


# --- CERTIFICATIONS ---
certifications = [
    ['''##### **[Advanced Learning Algorithms](https://www.coursera.org/account/accomplishments/verify/3TU4CH69L2SQ)**        
    \n - Built and trained a neural network with TensorFlow for multi-class classification.
    \n - Developed and utilized decision trees and tree ensemble methods.
    ''', f'###### Coursera, Feb 2024 \n [download pdf!](https://www.coursera.org/account/accomplishments/certificate/3TU4CH69L2SQ)'],
    
    ['''##### **[Supervised Machine Learning: Regression and Classification](https://www.coursera.org/account/accomplishments/verify/GD5S7QU3S8ZP)** 
    \n - Built machine learning models in Python using NumPy & scikit-learn. 
    \n - Built and trained supervised models for regression and classification tasks.
    ''', '###### Coursera, Feb 2024 \n [download pdf!](https://www.coursera.org/account/accomplishments/certificate/GD5S7QU3S8ZP)'],
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



# --- CONTACT FORM ---
contact_form = """
<form action="https://formsubmit.co/alimomeni2000.official@gmail.com" method="POST">
    <input type="text" name="name" placeholder="Your Name" required>
    <input type="email" name="email" placeholder="Your Email" required>
    <textarea name="message" placeholder="Your Message" rows="4" required></textarea>
    <button type="submit">Send</button>
</form>
"""

