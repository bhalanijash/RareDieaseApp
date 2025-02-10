#!/bin/bash

# Install dependencies
pip install --upgrade pip
pip install -r requirements.txt

# Run the Flask app with Gunicorn
gunicorn app:app