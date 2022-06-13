#!/bin/bash
echo 'Installing packages'
sudo apt install python3 python3-pip python3-venv -y
echo 'Setting up venv'
python3 -m venv venv
source venv/bin/activate
echo 'Installing dependancies'
pip3 install -r requirements.txt
echo 'Running unit tests'
python3 -m pytest --cov=application --cov-report=html
echo 'Copying files'
ssh jenkins@app-server 
rm -r application/
rm app.py
rm create.py
exit
scp -r application/ jenkins@app-server:/home/jenkins/application
scp app.py jenkins@app-server:/home/jenkins
scp create.py jenkins@app-server:/home/jenkins
scp requirements.txt jenkins@app-server:/home/jenkins
echo "Deploying app"
ssh jenkins@app-server < deploy.sh
