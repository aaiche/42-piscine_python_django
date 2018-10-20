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

# version de pip3
pip3 --version

#
# on demande la version de devlpt, cf.  https://github.com/jaraco/path.py.git, puis pargraphe Development
# help de pip3:
# 	--log <path>		--> Path to a verbose appending log.
#	-t,--target <dir> 	-->	Install packages into <dir>.
#	-U, --upgrade		--> Upgrade all packages to the newest available version. This
#			                process is recursive regardless of whether a dependency is already satisfied.
#	--force-reinstall	--> When upgrading, reinstall all packages even if they are already up-to-date.
#


#
# avec mon env. j ai un ptit souci lors de l install de ce module au autre
# workaround: cf. https://stackoverflow.com/questions/24257803/distutilsoptionerror-must-supply-either-home-or-prefix-exec-prefix-not-both/37644135
# 		add to ~/.pydistutils.cfg: 
# 			[install]
#			prefix=
#
pip3 install --force-reinstall --upgrade --target local_lib git+https://github.com/jaraco/path.py.git --log path_module_install.log
python3 ./my_program.py
