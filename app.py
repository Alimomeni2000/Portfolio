import streamlit as st
from pathlib import Path
from PIL import Image
from streamlit_lottie import st_lottie
import base64
from io import BytesIO
from reader import *
from pathlib import Path
import requests
import nbformat
from nbconvert import HTMLExporter

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

def convert_notebook_from_github(raw_url):
    # Fetch the notebook content from the GitHub raw link
    response = requests.get(raw_url)
    if response.status_code == 200:
        notebook_content = response.text
        notebook = nbformat.reads(notebook_content, as_version=4)

        # Convert the notebook to HTML
        html_exporter = HTMLExporter()
        body, _ = html_exporter.from_notebook_node(notebook)

        return body
    else:
        return "Error: Unable to fetch the notebook from GitHub."

def main(url,project_id):
    st.title(f"Jupyter Notebook Viewer - Project {project_id}")
    
    # Use the correct raw URL for the notebook
    raw_url = url#"https://raw.githubusercontent.com/Alimomeni2000/Black-Friday-Sale/main/Black%20Friday%20Sale.ipynb"
    
    # Fetch and display the notebook
    html_content = convert_notebook_from_github(raw_url)
    
    # Use a unique session state key for each project_id to track showing/hiding
    state_key = f'show_notebook_{project_id}'
    if state_key not in st.session_state:
        st.session_state[state_key] = False

    # Column layout for buttons and messages
    col1, col2 = st.columns(2, gap="small")

    with col1:
        # Create a custom button style
        button_label = "Click to Show/Hide Notebook"
        
        # Add a unique key for each button by using the project_id
        if st.button(button_label, key=f"toggle_notebook_{project_id}"):
            st.session_state[state_key] = not st.session_state[state_key]

    if st.session_state[state_key]:
        # Display notebook content as HTML
        st.components.v1.html(html_content, height=800, scrolling=True)
    else:
        with col2:
            st.write("Notebook content is hidden. Click the button to show it.")



current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV.pdf"
profile_pic_path = current_dir / "assets" / "profile-pic.png"

with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)

with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()





class ResumeApp:
    def __init__(self):
        self.current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
        self.css_file = self.current_dir / "styles" / "main.css"
        self.resume_file = self.current_dir / "assets" / "CV.pdf"
        self.profile_pic_path = self.current_dir / "assets" / "profile-pic.png"
        self.page_setup()

    def page_setup(self):
        """Set up page settings."""
        # st.set_page_config(page_title="Digital CV | Ali Momeni", page_icon=":wave:")
        with open(self.css_file) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
        self.load_resume()

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
        st.markdown('<hr style="height:2px;border:none;color:#f2f3f4;background-color:#f2f3f4;" />', unsafe_allow_html=True)

    def display_edcuation(self):
        
        st.markdown("<div id='education'></div>", unsafe_allow_html=True)
        st.title("Education")
        st.write('\n')
        txt(uni_place[0], uni_place[1],[6,2.5])
        st.markdown(uni_education)


        txt(high_place[0],high_place[1],[6,2.5])
        st.markdown(high_education)
        st.markdown('<hr style="height:2px;border:none;color:#f2f3f4;background-color:#f2f3f4;" />', unsafe_allow_html=True)



    def download_resume_button(self):
        """Add a button to download the resume."""
        col1, col2 = st.columns(2, gap="small")
        with col1:
            st.download_button(
                label="📄 Download Resume",
                data=self.PDFbyte,
                file_name="Ali_Momeni_Resume.pdf",
                mime="application/octet-stream",
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
        st.markdown('<hr style="height:2px;border:none;color:#f2f3f4;background-color:#f2f3f4;" />', unsafe_allow_html=True)
    
    def display_experience(self):
        st.title("Experience")
        st.write("### - Academic")
        for i in range(len(experiences_academic)):
            txt(experiences_academic[i][0], experiences_academic[i][1], [3.5, 1])
            # if i < len(experince) - 1:
        st.markdown('<hr style="border: none; border-top: 1px dotted #d6dbdf; margin: 20px 0;" />', unsafe_allow_html=True)
        st.write("### - Professional")
        txt(experiences_professional[0][0], experiences_professional[0][1], [3, 1])
        st.markdown('<hr style="height:2px;border:none;color:#f2f3f4;background-color:#f2f3f4;" />', unsafe_allow_html=True)

    def display_skills(self):
        """Display skills section."""
        st.title("Skills")
        for s in skills_list:
            txt(s[0], s[1], [1, 2])
        st.markdown('<hr style="height:2px;border:none;color:#f2f3f4;background-color:#f2f3f4;" />', unsafe_allow_html=True)

    def display_certifications(self):
        """Display certifications section."""
        st.title("Certifications")
        for i in range(len(certifications)):
            txt(certifications[i][0], certifications[i][1], [3.5, 1])
            if i < len(certifications) - 1:
                st.markdown('<hr style="border: none; border-top: 1px dotted #d6dbdf; margin: 20px 0;" />', unsafe_allow_html=True)
        st.markdown('<hr style="height:2px;border:none;color:#f2f3f4;background-color:#f2f3f4;" />', unsafe_allow_html=True)

    def display_projects(self):
        """Display the projects section."""
        st.title("Projects")
        for i in range(len(professional_projects)):
            txt(professional_projects[i][0], professional_projects[i][1], [2.5, 1])
            main(professional_projects[i][2],i)
            st.markdown('<hr style="border: none; border-top: 1px dotted #d6dbdf; margin: 20px 0;" />', unsafe_allow_html=True)

        st.markdown('<hr style="height:2px;border:none;color:#f2f3f4;background-color:#f2f3f4;" />', unsafe_allow_html=True)

    def display_references(self):
        """Display the references section."""
        st.title("References")
        st.markdown(references, unsafe_allow_html=True)
        st.markdown('<hr style="height:2px;border:none;color:#f2f3f4;background-color:#f2f3f4;" />', unsafe_allow_html=True)

    def display_contact(self):
        """Display the contact section with social media and form."""
        st.title("Contact")
        list_socialmedia_animation = {
            'linkedin': 'https://www.linkedin.com/in/ali-momeni-b490bb206/',
            'github': 'https://github.com/Alimomeni2000/',
            'telegram': 'https://t.me/alimomeni00',
            'instagram': 'https://www.instagram.com/alimomeni9979',
        }
        cols = st.columns(len(list_socialmedia_animation))
        for col, (platform, url) in zip(cols, list_socialmedia_animation.items()):
            lottie_animation = load_lottie_json(f'./assets/{platform}.json')
            with col:
                st_lottie(lottie_animation, width=100, height=100)
                st.markdown(f'<a href="{url}" target="_blank"></a>', unsafe_allow_html=True)

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

# Run the app
if __name__ == "__main__":
    app = ResumeApp()
    app.run()
