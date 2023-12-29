#!/bin/bash
python -m venv venv
venv/scripts/activate
pip install -r python-client/requirements.txt
python python-client/app/app.py
