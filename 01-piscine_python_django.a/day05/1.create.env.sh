#!/bin/sh

#je verifie que j utilise le bon python
	# less ~
	#e1r6p4% less ~/.zshrc
	#	...
	#	export PATH=$HOME/.brew/bin:$PATH
	#	# Load Homebrew config script
	#	source $HOME/.brewconfig.zsh
	#
	#e1r6p4% source ~/.zshrc
	#e1r6p4% which python3
	#	/Users/aaiche/.brew/bin/python3
	#e1r6p4% python --version
	#		Python 2.7.10
	#e1r6p4% python3 --version
	#	Python 3.6.5

# je verifie que virtualenv est installe, sinon pip3 install virtualenv
	#e1r6p4% which pip3
	#	/Users/aaiche/.brew/bin/pip3


#je cree mon environt virtuel
	#e1r6p4% virtualenv -p /Users/aaiche/.brew/bin/python3 mon_env_virtuel

# j active mon_env_virtuel
	#e1r6p4% source mon_env_virtuel/bin/activate
	#(mon_env_virtuel) e1r6p4%

# je regarde ce que j ai comme packages
	# (mon_env_virtuel) e1r6p4% pip list
	#	Package    Version
	#	---------- -------
	#	pip        10.0.1
	#	setuptools 39.2.0
	#	wheel      0.31.1

# je verifie quel est le python que j utilise
	#(mon_env_virtuel) e1r6p4% which python
		#/Users/aaiche/wip/piscine_python/day04.a/ex00/mon_env_virtuel/bin/python
	#(mon_env_virtuel) e1r6p4% python --version
		#Python 3.6.5

# j installe django meme version que la video
	# (mon_env_virtuel) e1r6p4% pip install django==1.9.7

	#(mon_env_virtuel) e1r6p4% pip list
	#	Package    Version
	#	---------- -------
	#	Django     1.9.7
	#	pip        10.0.1
	#	setuptools 39.2.0
	#	wheel      0.31.1

#je sauveragde mes pre-requis
#	(mon_env_virtuel) e1r6p4% pip freeze --local > requirements.txt
#	(mon_env_virtuel) e1r6p4% cat requirements.txt
#		Django==1.9.7

# et maintenant je clean et je le fais la derniere partie en script

echo "source ~/.zshrc"
source ~/.zshrc
echo "virtualenv -p /Users/aaiche/.brew/bin/python3 mon_env_virtuel"
virtualenv -p /Users/aaiche/.brew/bin/python3 mon_env_virtuel
echo "source mon_env_virtuel/bin/activate"
source mon_env_virtuel/bin/activate
echo "pip3 install -r requirements.txt"
pip3 install -r requirements.txt
echo "----------------------------"
echo "refaire en command prompt:"
echo "           "
echo "source mon_env_virtuel/bin/activate"
echo "----------------------------"
source mon_env_virtuel/bin/activate
