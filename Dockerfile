# Use the official lightweight Python image  
FROM python:3.12  

# Set the working directory in the container  
WORKDIR /app  

# Copy the requirements.txt file into the container at /app  
COPY requirements.txt .  

# Install any necessary packages specified in requirements.txt  
RUN pip install --no-cache-dir -r requirements.txt  

# Copy the rest of the application code to the container  
COPY . .  

# Expose the port that Streamlit will run on  
EXPOSE 8501  

# Command to run the Streamlit app  
CMD ["streamlit", "run", "app.py"]