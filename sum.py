# import streamlit as st
# import nbformat
# import io
# import base64
# import matplotlib.pyplot as plt

# # Function to read the Jupyter Notebook and extract code cells
# def read_notebook(notebook_path):
#     with open(notebook_path, 'r', encoding='utf-8') as f:
#         notebook_content = nbformat.read(f, as_version=4)

#     cells = notebook_content['cells']
#     input_output_pairs = []

#     for cell in cells:
#         if cell['cell_type'] == 'code':
#             input_code = cell['source']
#             input_output_pairs.append((input_code, None))  # We'll execute to get outputs

#     return input_output_pairs

# # Function to execute code and capture output (including plots) in a shared global context
# def execute_code(code, global_vars):
#     output_text = ""
#     plot_images = []

#     try:
#         # Capture standard output and any exceptions
#         exec(code, global_vars)
#     except Exception as e:
#         output_text = str(e)

#     # Capture the plot if matplotlib is used
#     if plt.get_fignums():
#         # Convert the plot to a PNG image
#         buf = io.BytesIO()
#         plt.savefig(buf, format='png')
#         buf.seek(0)
#         plot_image = base64.b64encode(buf.read()).decode('utf-8')
#         plot_images.append(plot_image)
#         buf.close()
#         plt.close()

#     return output_text, plot_images

# # Streamlit UI
# st.title("Display Jupyter Notebook Content with Plots")

# # Upload notebook file
# # uploaded_file = './projects/cloned_repo/Black Friday Sale.ipynb'
# uploaded_file = st.file_uploader("Upload a Jupyter Notebook (.ipynb)", type="ipynb")

# if uploaded_file is not None:
#     # Save the uploaded file temporarily
#     with open("temp_notebook.ipynb", "wb") as f:
#         f.write(uploaded_file.getbuffer())

#     st.success("Notebook uploaded successfully!")

#     # Read the notebook and extract inputs (code cells)
#     input_output_pairs = read_notebook("./BlackFridaySale.ipynb")

#     # Create a shared global execution context
#     global_vars = {}

#     # Display and execute the input cells
#     for i, (input_code, _) in enumerate(input_output_pairs):
#         st.subheader(f"Input Cell {i + 1}")
#         st.code(input_code, language='python')  # Display input code

#         # Execute the code and capture the output and any plot images
#         output_text, plot_images = execute_code(input_code, global_vars)

#         # Display the output text, if any
#         if output_text:
#             st.subheader(f"Output Cell {i + 1}")
#             st.text(output_text)

#         # Display the plot images, if any
#         for plot_image in plot_images:
#             st.subheader(f"Plot from Cell {i + 1}")
#             st.image(f"data:image/png;base64,{plot_image}", caption="Generated Plot")

import streamlit as st
import nbformat
import io
import base64
import matplotlib.pyplot as plt
import sys

# Function to read the Jupyter Notebook and extract code cells
def read_notebook(notebook_path):
    with open(notebook_path, 'r', encoding='utf-8') as f:
        notebook_content = nbformat.read(f, as_version=4)

    cells = notebook_content['cells']
    input_output_pairs = []

    for cell in cells:
        if cell['cell_type'] == 'code':
            input_code = cell['source']
            input_output_pairs.append((input_code, None))  # We'll execute to get outputs

    return input_output_pairs

# Function to execute code and capture output (including plots and printed output)
def execute_code(code, global_vars):
    output_text = ""
    plot_images = []

    # Capture the standard output (e.g., print statements, df.info())
    temp_stdout = io.StringIO()
    sys.stdout = temp_stdout  # Redirect the stdout to our StringIO object

    try:
        # Execute the code in the global execution context
        exec(code, global_vars)
        output_text = temp_stdout.getvalue()  # Get the captured output
    except Exception as e:
        output_text = str(e)

    # Restore the default stdout
    sys.stdout = sys.__stdout__

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
st.title("Display Jupyter Notebook Content with Plots")

# Upload notebook file
uploaded_file = st.file_uploader("Upload a Jupyter Notebook (.ipynb)", type="ipynb")

if uploaded_file is not None:
    # Save the uploaded file temporarily
    with open("temp_notebook.ipynb", "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.success("Notebook uploaded successfully!")

    # Read the notebook and extract inputs (code cells)
    input_output_pairs = read_notebook("temp_notebook.ipynb")  # Use the temporary file

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
