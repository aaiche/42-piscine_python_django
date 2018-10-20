#!/bin/sh

virtualenv django_venv
source django_venv/bin/activate
pip3 install -r requirement.txt
