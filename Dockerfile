# Use a base image with Python installed
FROM python:3.9

# Set working directory in the container
WORKDIR /app

# Install necessary dependencies
RUN apt-get update && apt-get install -y \
    python3-opencv \
    # Additional dependencies may include:
    # libsm6 libxext6 libxrender-dev
    # Other libraries required by OpenCV or dlib
    && pip install opencv-python-headless


# Copy your face detection app code into the container
COPY . /app

# Set the command to run your app
CMD ["python", "app.py"]
