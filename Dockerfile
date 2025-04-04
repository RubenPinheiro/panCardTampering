# Use an official lightweight Python image
FROM python:3.12-slim

# Install OpenCV dependencies
RUN apt-get update && apt-get install -y \
    libgl1 \
    libgl1-mesa-glx \
    libglib2.0-0 \
    libsm6 \
    libxext6 \
    libxrender1 \
    libfontconfig1 \
    && rm -rf /var/lib/apt/lists/*

# Set the working directory
WORKDIR /app

# Copy project files
COPY . .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port Railway uses
EXPOSE 8080

# Start the application
CMD ["gunicorn", "app:app('DevelopmentConfig')", "--timeout", "60"]
