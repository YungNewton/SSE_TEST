# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory
WORKDIR /usr/src/app

# Install system dependencies and ffmpeg
RUN apt-get update && apt-get install -y \
    build-essential \
    ffmpeg \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements.txt and install Python dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Expose the port the app runs on
EXPOSE 5000

# Define the command to run the app
CMD ["python", "app.py"]
