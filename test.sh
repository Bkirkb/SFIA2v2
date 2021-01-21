#!/bin/bash
sudo apt-get update
sudo apt install -y python3 python3-venv python3-pip

python3 -m venv venv
source venv/bin/activate
pip3 install -r service1/requirements.txt
pip3 install flask_testing pytest pytest-cov
python3 -m pyte