#!/bin/bash
sudo apt-get update
sudo apt install -y python3 python3-venv python3-pip

python3 -m venv venv
source venv/bin/activate
pip3 install -r jenkins/requirements.txt
pip3 install flask_testing pytest pytest-cov
python3 -m pytest --cov=service1/application --cov=service2 --cov=service3 --cov=service4 --cov-report xml --cov-report term-missing --junitxml junit.xml
deactivate
