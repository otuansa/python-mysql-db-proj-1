#!/bin/bash
# set -e  # Exit immediately on error
PROJECT_DIR="/home/ubuntu/python-mysql-db-proj-1"
cd "$PROJECT_DIR"

# Ensure necessary packages are installed
sudo apt-get update
sudo apt-get install -y python3.12-venv

# Create a virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    python3 -m venv venv
fi

# Activate the virtual environment
source venv/bin/activate

# Upgrade pip and install requirements
pip install --upgrade pip
pip install -r requirements.txt

# Ensure Flask app will run on 0.0.0.0
# (this should be in your app.py)

# Start the Flask app in the background and log output
nohup python3 app.py > /home/ubuntu/app.log 2>&1 &
