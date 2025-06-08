#!/bin/bash
set -e

cd /home/ubuntu/python-mysql-db-proj-1

sudo apt-get update
sudo apt-get install -y python3.12-venv

python3 -m venv venv
source venv/bin/activate
pip install flask pymysql

# Start Flask app in background
nohup python3 app.py > /home/ubuntu/flask.log 2>&1 &
