import streamlit as st
import streamlit.components.v1 as components

st.title("Jupyterlite in Streamlit")
st.sidebar.header("Configuration")
components.iframe(
    "https://jupyterlite.github.io/demo/repl/index.html?kernel=python&toolbar=1",
    height=500
)


# import streamlit as st
# import requests
# import nbformat
# from nbconvert import HTMLExporter

# def convert_notebook_from_github(raw_url):
#     # Fetch the notebook content from the GitHub raw link
#     response = requests.get(raw_url)
#     if response.status_code == 200:
#         notebook_content = response.text
#         notebook = nbformat.reads(notebook_content, as_version=4)

#         # Convert the notebook to HTML
#         html_exporter = HTMLExporter()
#         body, _ = html_exporter.from_notebook_node(notebook)

#         return body
#     else:
#         return "Error: Unable to fetch the notebook from GitHub."

# def main():
#     st.title("Jupyter Notebook Viewer")

#     # GitHub raw URL of the notebook
#     raw_url = "https://raw.githubusercontent.com/Alimomeni2000/Black-Friday-Sale/main/Black%20Friday%20Sale.ipynb"

#     # Initialize session state if not already done
#     if 'show_notebook' not in st.session_state:
#         st.session_state.show_notebook = False

#     # Determine button label based on the visibility state
#     button_label = "Click to hide" if st.session_state.show_notebook else "Click to show"

#     # Button to toggle notebook visibility
#     if st.button(button_label):
#         # Toggle the session state
#         st.session_state.show_notebook = not st.session_state.show_notebook

#     # Use the session state to control whether to display the notebook
#     if st.session_state.show_notebook:
#         st.write("Loading notebook from GitHub...")
#         html_content = convert_notebook_from_github(raw_url)
#         st.components.v1.html(html_content, height=800, scrolling=True)
#     else:
#         st.write("Notebook content is hidden. Click the button to show it.")

# if __name__ == "__main__":
#     main()
