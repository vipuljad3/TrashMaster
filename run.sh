#!/bin/sh
echo 'creating virtual env venv'
python3 -m venv venv
source venv/bin/activate
echo 'Installing required libraries'
pip install -r requirements.txt
chmod 755 main.py
echo 'Running App'
export FLASK_APP=main.py
export FLASK_RUN_PORT=8000
python3 -m flask run 