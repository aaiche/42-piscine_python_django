#!/bin/bash

#installer python3 en local cf ~/.brew
#	brew install python3
#	source ~/.zshrc
#	which python3
#	which pip3
#
#installer virtualenv en local cf ~/.brew
#	pip3 list
#	pip3 install virtualenv
#	pip3 list
#	source ~/.zshrc
#
#creer nouvel environnement
#	virtualenv monNouveauEnvVirtual
#
#activer le nouvel environnement
#	source monNouveauEnvVirtual/bin/activate
#
# NE FONCTIONNE PAS python3 -m monNouveauEnvVirtual "/Users/aaiche/wip/piscine_python/day03.a/ex01/localdb"
# 
# 
# script demande
pip3 -V
pip3 install --force-reinstall --upgrade -t local_lib git+https://github.com/jaraco/path.py.git --log file.log
python3 ./my_program.py
