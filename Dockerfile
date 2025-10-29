# Use an official lightweight Python image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy your Python script into the container
COPY . .

# Install dependencies
RUN pip install --no-cache-dir requests

# Command to run your script
CMD ["python", "app.py"]
