#!/bin/bash
python -m venv venv
venv/scripts/activate
pip install -r requirements.txt
python python-client/api/index.py
