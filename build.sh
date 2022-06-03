#!/bin/bash
# Installing packages
sudo apt install python3 python3-pip python3-venv -y
# Setting up vene
python3 -m venv venv
source venv/bin/activate
# Installing dependancies
pip3 install -r requirements.txt
# Running unit tests
python3 -m pytest --cov=application --cov-report=html
# Copying files
scp -r . jenkins@app-server:/home/jenkins/app
# Deploying app
ssh jenkins@app-server < deploy.sh
