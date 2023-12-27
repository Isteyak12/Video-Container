# Use an official Python runtime as a parent image
FROM python:3

# Set the working directory in the container
WORKDIR /app

# Copy the Python script into the container at /app
COPY your_script_name.py /app/

# Install OpenCV and other dependencies
RUN pip install opencv-python-headless

# Run the Python script when the container launches
CMD ["python", "app.py"]
