#!/bin/bash
sudo apt update
sudo apt install python3 python3-pip python3-venv gunicorn -y
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
python3 create.py
gunicorn --workers 4 --bind 0.0.0.0:5000 app:app 
