import streamlit as st
from pathlib import Path
from PIL import Image
from streamlit_lottie import st_lottie
import base64
from io import BytesIO
from reader import *

# import requests
# import nbformat
# from nbconvert import HTMLExporter

st.cache_data.clear()  

st.set_page_config(
    page_title="Digital CV | Ali Momeni",
    page_icon="📄"
)
# Define custom background with CSS
page_bg_img = """
<style>
[data-testid="stMainBlockContainer"]{
background-color: #ffffff;
opacity: 1;
background-size: 5px 5px;
}
</style>
"""
# Custom CSS for shadow effects  
st.markdown("""  
<style>  
.sidebar .sidebar-content {  
    box-shadow: 5px 5px 10px rgba(0, 0, 0, 0.5);  
    background-color: #ffffff;  /* Keep your sidebar background */  
}  
[data-testid="stAppViewContainer"] {  
    box-shadow: 5px 5px 10px rgba(0, 0, 0, 0.5);  
} 
[data-testid="stAlertContainer"]{
            color:#000000;}  
</style>  
""", unsafe_allow_html=True)  
# Apply custom background style
st.markdown(page_bg_img, unsafe_allow_html=True)

st.markdown(  
    """  
    <style>  
    .stMainBlockContainer {  
        /* Background Image Example */  
        background-size: cover; /* Cover the entire area */  
        background-repeat: no-repeat; /* Prevent the image from repeating */  
        padding: 20px; /* Add some inner padding */  
        border-radius: 8px; /* Optional: rounded corners */  
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.5); /* Add shadow effect */  
    }  
    </style>  
    """,  
    unsafe_allow_html=True  
)  


# Load assets like CSS, profile picture, and resume only once.
@st.cache_resource
def load_assets():
    current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
    css_file = current_dir / "styles" / "main.css"
    resume_file = current_dir / "assets" / "CV.pdf"
    profile_pic_path = current_dir / "assets" / "profile-pic.png"
    with open(css_file) as f:
        css_content = f.read()
    with open(resume_file, "rb") as pdf_file:
        resume_pdf = pdf_file.read()
    profile_pic = Image.open(profile_pic_path)
    return css_content, resume_pdf, profile_pic

css_content, resume_pdf, profile_pic,= load_assets()
st.markdown(f"<style>{css_content}</style>", unsafe_allow_html=True)

# --- CACHE LOTTIE ANIMATIONS ---
@st.cache_data
def get_image_as_base64(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()


class ResumeApp:
    def __init__(self):
        self.current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
        self.css_file = self.current_dir / "styles" / "main.css"
        self.resume_file = self.current_dir / "assets" / "CV.pdf"
        self.profile_pic_path = self.current_dir / "assets" / "profile-pic.png"
        self.page_setup()

    def page_setup(self):
        with open(self.css_file) as f:
            st.markdown(f"<style>{f.read()}</style>",unsafe_allow_html=True)
     

    def load_resume(self):
        """Load resume data."""
        with open(self.resume_file, "rb") as pdf_file:
            self.PDFbyte = pdf_file.read()
    def load_profile_pic(self):
        """Load and display profile picture."""
        profile_pic = Image.open(self.profile_pic_path)
        return profile_pic

    def display_navbar(self):
        """Display the navigation bar."""
        st.markdown(navbar, unsafe_allow_html=True)

    def display_about(self):
        """Display the About section."""
        st.markdown("<div id='about'></div>", unsafe_allow_html=True)
        st.title("About Me")
        col1, col2 = st.columns(2, gap="small")
        with col1:
            st.image(self.load_profile_pic(), width=380)
        with col2:
            st.title("Ali Momeni")
            st.info(DESCRIPTION)

        st.write('\n')
        self.download_resume_button()
        st.markdown('<hr style="height:2px;border:none;color:#020304;background-color:#020304;" />', unsafe_allow_html=True)

    def display_edcuation(self):
        
        st.markdown("<div id='education'></div>", unsafe_allow_html=True)
        st.title("Education")
        st.write('\n')
        try:
            txt(uni_place[0], uni_place[1],[6,2.5])
        except:
            pass
        st.markdown(uni_education)


        txt(high_place[0],high_place[1],[6,2.5])
        st.markdown(high_education)
        st.markdown('<hr style="height:2px;border:none;color:#020304;background-color:#020304;" />', unsafe_allow_html=True)



    def download_resume_button(self):
        """Add a button to download the resume."""
        col1, col2 = st.columns(2, gap="small")
        with col1:
            resume_link = "https://docs.google.com/document/d/18rEjwRZ8yOaSlklZ2P5Acg0saMESWrux/export?format=pdf"  

# Use st.markdown to create a button-style link  
            st.markdown(  
    f"""  
    <a href="{resume_link}" target="_blank" style="text-decoration: none;">  
        <div style="  
            display: inline-block;   
            padding: 9px 16px;   
            background: linear-gradient(45deg, #4CAF50, #81C784);   
            color: white;   
            border-left:1inpx;
            border-radius: 25px;   
            font-weight: bold;   
            text-align: center;   
            box-shadow: 0 4px 10px rgba(0,0,0,0.2);   
            transition: all 0.3s ease;  
        ">  
           📄 Download Resume  
        </div>  
    </a>  
    <style>  
        a div:hover {{  
            background: linear-gradient(45deg, #388E3C, #66BB6A);  
            transform: scale(1.05);  
        }}  
    </style>  
    """,  
    unsafe_allow_html=True  
) 
        with col2:
            self.display_email()

    def display_email(self):
        """Display the email contact with an icon."""
        def img_to_base64(image: Image.Image) -> str:
            buffered = BytesIO()
            image.save(buffered, format="PNG")
            img_str = base64.b64encode(buffered.getvalue()).decode("utf-8")
            return img_str

        profile_pic = Image.open("./assets/gmail.png")
        image_base64 = img_to_base64(profile_pic)
        image_html = f'<img src="data:image/png;base64,{image_base64}" width="60" height="50" style="border-radius: 25%;">'
        combined_html = f"""
            <div style="display: flex; align-items: center;">
                {image_html}
                <a href="mailto:{EMAIL}"><span style="font-size: 20px;margin-left: 15px;">alimomeni2000.official@gmail.com</span></a>
            </div>
        """
        st.markdown(combined_html, unsafe_allow_html=True)

    def display_research_interests(self):
        st.title("Research Interests")
        st.markdown(research_interests)
        st.markdown('<hr style="height:2px;border:none;color:#020304;background-color:#020304;" />', unsafe_allow_html=True)
    
    def display_experience(self):
        st.title("Experience")
        st.write("### - Academic")
        for i in range(len(experiences_academic)):
            txt(experiences_academic[i][0], experiences_academic[i][1], [3.5, 1])
            # if i < len(experince) - 1:
        st.write("### - Professional")
        txt(experiences_professional[0][0], experiences_professional[0][1], [3, 1])
        st.markdown('<hr style="height:2px;border:none;color:#020304;background-color:#020304;" />', unsafe_allow_html=True)

    def display_skills(self):
        """Display skills section."""
        st.title("Skills")
        for s in skills_list:
            txt(s[0], s[1], [1, 2])
        st.markdown('<hr style="height:2px;border:none;color:#020304;background-color:#020304;" />', unsafe_allow_html=True)

    def display_certifications(self):
        """Display certifications section."""
        st.title("Certifications")
        for i in range(len(certifications)):
            txt(certifications[i][0], certifications[i][1], [3.5, 1])
        # st.write()
            # if i < len(certifications) - 1:
                
            #     st.markdown('<hr style="border: none; border-top: 1px dotted #d6dbdf; margin: 20px 0;" />', unsafe_allow_html=True)
        st.markdown('<hr style="height:2px;border:none;color:#020304;background-color:#020304;" />', unsafe_allow_html=True)

    def display_projects(self):
        """Display the projects section."""
        st.title("Professional Projects")
        for i in range(len(professional_projects)):
            txt(professional_projects[i][0], professional_projects[i][1], [3, 1])
            # main(professional_projects[i][2],i)
        st.markdown('<hr style="height:2px;border:none;color:#020304;background-color:#020304;" />', unsafe_allow_html=True)

        st.title("Academic Projects")
        for i in range(len(academic_projcts)):
            txt(academic_projcts[i][0], academic_projcts[i][1], [3, 1])

        st.markdown('<hr style="height:2px;border:none;color:#020304;background-color:#020304;" />', unsafe_allow_html=True)

    def display_references(self):
        """Display the references section."""
        st.title("References")
        st.markdown(references, unsafe_allow_html=True)
        st.markdown('<hr style="height:2px;border:none;color:#020304;background-color:#020304;" />', unsafe_allow_html=True)

    def display_contact(self):
        """Display the contact section with social media and form."""
        st.title("Contact")
        list_socialmedia = {
            'linkedin': 'https://www.linkedin.com/in/ali-momeni-b490bb206/',
            'github': 'https://github.com/Alimomeni2000/',
            'telegram': 'https://t.me/alimomeni00',
            'instagram': 'https://www.instagram.com/alimomeni9979',
        }
        # Display your social media icons  
        cols = st.columns(len(list_socialmedia))  


        for col, (platform, url) in zip(cols, list_socialmedia.items()):
            with col:
                image_path = f'./assets/{platform}.png'  # Ensure this path is correct
                try:
                    # Convert the image to base64
                    img_base64 = get_image_as_base64(image_path)
                    
                    # Display clickable image
                    st.markdown(f"""
                        <a href="{url}" target="_blank">
                            <img src="data:image/png;base64,{img_base64}" alt="{platform}" style="width:100px; height:100px; object-fit:cover;">
                        </a>
                    """, unsafe_allow_html=True)

                except Exception as e:
                    st.error(f"Error loading image: {e}")
        st.write('\n')
        col1, col2 = st.columns([2, 1])
        with col2:
            lottie_animation = load_lottie_json('./assets/Animation - 1728895738988.json')
            st_lottie(lottie_animation, width=350, height=350)
        with col1:
            st.markdown(contact_form, unsafe_allow_html=True)
    def run(self):
        """Run the Streamlit app."""
        self.display_navbar()
        self.display_about()
        self.display_edcuation()     
        self.display_research_interests()
        self.display_experience()
        # self.display_section('research_interests', "Research Interests", research_interests)
        self.display_skills()
        self.display_certifications()
        self.display_projects()
        self.display_references()
        self.display_contact()
        footer = """  
            <style>  
                .footer {  
                    position: fixed;  
                    left: 0;  
                    bottom: 0;  
                    width: 100%;  
                    background-color: #f1f1f1;  
                    text-align: center;  
                    padding: 10px;  
                    font-size: 12px;  
                    color: #555;  
                }  
            </style>  
            <div class="footer">  
                © 2024 Your Ali Momeni. All rights reserved.  
            </div>  
        """  

        # Render the footer  
        st.markdown(footer, unsafe_allow_html=True)  
        st.markdown(  
        """  
        <style>/* Fixed "Go Up" button on the right side */
        .go-up-btn {  
            position: fixed;  
            right: 20px;  
            bottom: 50px;  
            background-color: #333;  
            color: white;  
            padding: 10px 20px;  
            border-radius: 5px;  
            text-decoration: none;  
            z-index: 1000;  /* Keep above other elements */  
            font-size: 14px;  
            transition: background-color 0.3s;  
        }  
        .go-up-btn:hover {  
            background-color: #575757;  
        }  
        </style>  

        <!-- "Go Up" button -->
        <a href="#about" class="go-up-btn" id="go-up-btn">Go Up</a>  

        <script>
        // JavaScript function to scroll to the top when "Go Up" is clicked
        document.getElementById("go-up-btn").onclick = function() {
            window.scrollTo({top: 0, behavior: 'smooth'});
        }
        </script>
        """,  
        unsafe_allow_html=True  
    )  

app = ResumeApp()
app.run()

#