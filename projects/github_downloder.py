import streamlit as st
import requests
import base64
import time
download_link=''
# Function to download file from a complete URL with retries
def download_file(url, retries=3, delay=2):
    for attempt in range(retries):
        try:
            response = requests.get(url)
            response.raise_for_status()  # Raise an error for bad responses (4xx or 5xx)
            return response.content
        except requests.exceptions.RequestException as e:
            if attempt < retries - 1:
                st.warning(f"Attempt {attempt + 1} failed: {e}. Retrying...")
                time.sleep(delay)
            else:
                st.error(f"Failed to fetch the file from the provided URL after {retries} attempts.")
                return None

# Convert bytes to a downloadable link
def create_download_link(file_content, file_name):
    b64 = base64.b64encode(file_content).decode()
    href = f'<a href="data:application/octet-stream;base64,{b64}" download="{file_name}">Download {file_name}</a>'
    return href

st.title("Download Jupyter Notebook from URL")

# Input for the complete URL
# url = st.text_input("Enter the complete URL of the .ipynb file")#, "https://raw.githubusercontent.com/username/repository/main/notebooks/example.ipynb")
# st.write(url)
url = "https://github.com/Alimomeni2000/Black-Friday-Sale/blob/main/Black%20Friday%20Sale.ipynb"
# Download button
st.write(url)

if st.button("Download Notebook"):
    file_content = download_file(url)

    if file_content:
        # Get the file name from the URL
        file_name = url.split("/")[-1]
        # Show the download link
        download_link = create_download_link(file_content, file_name)
        st.markdown(download_link, unsafe_allow_html=True)



import streamlit as st
import nbformat
import io
import base64
import matplotlib.pyplot as plt
import requests

# Function to fetch notebook from GitHub
def fetch_notebook_from_github(url):
    if 'github.com' in url:
        url = url.replace('github.com', 'raw.githubusercontent.com').replace('/blob/', '/')
    response = requests.get(url)
    if response.status_code == 200:
        return response.content.decode('utf-8')
    else:
        st.error("Failed to fetch the notebook. Check the URL.")
        return None

# Function to read the Jupyter Notebook and extract code cells
def read_notebook(notebook_content):
    notebook_content = nbformat.reads(notebook_content, as_version=4)
    cells = notebook_content['cells']
    input_output_pairs = []

    for cell in cells:
        if cell['cell_type'] == 'code':
            input_code = cell['source']
            input_output_pairs.append((input_code, None))  # We'll execute to get outputs

    return input_output_pairs

# Function to execute code and capture output (including plots) in a shared global context
def execute_code(code, global_vars):
    output_text = ""
    plot_images = []

    try:
        # Capture standard output and any exceptions
        exec(code, global_vars)
    except Exception as e:
        output_text = str(e)

    # Capture the plot if matplotlib is used
    if plt.get_fignums():
        # Convert the plot to a PNG image
        buf = io.BytesIO()
        plt.savefig(buf, format='png')
        buf.seek(0)
        plot_image = base64.b64encode(buf.read()).decode('utf-8')
        plot_images.append(plot_image)
        buf.close()
        plt.close()

    return output_text, plot_images

# Streamlit UI
st.title("Display Jupyter Notebook from GitHub with Plots")

# Input for GitHub URL
github_url = url #  'https://github.com/Alimomeni2000/Fake_True_News/blob/main/Fake_True_News.ipynb'#st.text_input("Enter the GitHub URL of the Jupyter Notebook (.ipynb):")

if github_url:
    notebook_content = fetch_notebook_from_github(github_url)
    notebook_content
    if notebook_content:
        st.success("Notebook fetched successfully from GitHub!")

        # Read the notebook and extract inputs (code cells)
        input_output_pairs = read_notebook(notebook_content)

        # Create a shared global execution context
        global_vars = {}

        # Display and execute the input cells
        for i, (input_code, _) in enumerate(input_output_pairs):
            st.subheader(f"Input Cell {i + 1}")
            st.code(input_code, language='python')  # Display input code

            # Execute the code and capture the output and any plot images
            output_text, plot_images = execute_code(input_code, global_vars)

            # Display the output text, if any
            if output_text:
                st.subheader(f"Output Cell {i + 1}")
                st.text(output_text)

            # Display the plot images, if any
            for plot_image in plot_images:
                st.subheader(f"Plot from Cell {i + 1}")
                st.image(f"data:image/png;base64,{plot_image}", caption="Generated Plot")
