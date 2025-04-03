#!/bin/bash

# Install system dependencies
apt-get update && apt-get install -y \
    libgl1-mesa-glx \
    libsm6 \
    libxext6 \
    libxrender-dev \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
pip install -r requirements.txt

# Start the application
exec gunicorn "app:app('DevelopmentConfig')" --timeout 60
