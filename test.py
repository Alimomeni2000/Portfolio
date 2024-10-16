import streamlit as st

# Title of the project
st.title("My Python Project Showcase")

# Description of the project
st.write("""
This project demonstrates [Project Name], which is available on GitHub.
You can check out the full code here: 
""")

# GitHub link
st.markdown("[View the full project on GitHub](https://github.com/Alimomeni2000/Electricity_consumption_system_subscribers_Behbahan)")

st.subheader("Main Code Snippet")
code = '''
import pandas as pd

# Sample code from GitHub repository
data = pd.read_csv("data.csv")
print(data.head())
'''

st.code(code, language='python')
import requests

st.subheader("Main Code from GitHub")

url = "https://github.com/Alimomeni2000/Electricity_consumption_system_subscribers_Behbahan/blob/main/data_informations.py"
response = requests.get(url)
code = response.text

st.code(code, language='python')
