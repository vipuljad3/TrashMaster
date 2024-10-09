#!/bin/sh

chmod 755 main.py
source venv/bin/activate
export FLASK_APP=main.py
export FLASK_RUN_PORT=8000
python3 -m flask run 