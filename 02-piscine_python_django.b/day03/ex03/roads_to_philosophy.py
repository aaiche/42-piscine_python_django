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
#	virtualenv monNouveauEnvVirtuel
#
#activer le nouvel environnement
#	source monNouveauEnvVirtuel/bin/activate
#
#installer les packages requis cf. requirements.txt
#(monNouveauEnvVirtuel) e1r12p13% pip install Requests
#(monNouveauEnvVirtuel) e1r12p13% pip install BeautifulSoup4
# 
#preferer python3 a  #!/usr/bin/python3 car on utilise celui de la virtuelle
# 
# CORRECTION:
#   a) e1r12p13% virtualenv myNewEnv
#
#   b) e1r12p13% source myNewEnv/bin/activate
#       (myNewEnv) e1r12p13%
#
#   c) (myNewEnv) e1r12p13% pip3 install -r requirement.txt
#
#   d) (myNewEnv) e1r12p13% pip3 list
#
#   e) (myNewEnv) e1r12p13% python3 ...
#
#   f) (myNewEnv) e1r12p13% ll -rtl
#       ...
#       ...
#       
import sys
import requests
from bs4 import BeautifulSoup

def search_word(word):
    word = "_".join(word.split())
    print('word: %s ' % word)
    word_list = []
    while (1):
        if word == 'Philosophy':
            word_list.append(word)
            for c in word_list:
                print (c)
            print("{} roads from {} to {} !".format(len(word_list), word_list[0], word_list[-1]))
            return
        if word in word_list:
            print('It leads to an infinite loop !')
            return
        url = "https://en.wikipedia.org/wiki/" + word
        print('url: %s ' %url)
        r = requests.get(url)

        # traitement de http code not ok (=200)
        if r.status_code != 200:
            # 404: page n existe pas
            if r.status_code == 404:
                print("Nothing was found for {}".format(word))
                return
            else:
                # autre : donc a voir
                print("requete http donne un status: {}".format(r.status_code))
                return

        word_list.append(word)
        soup = BeautifulSoup(r.text, "html.parser")
        title = str(soup.find("title")).split('-', 1)[0].split('>', 1)[1].strip()
        s = soup.find('div', attrs={"id": "bodyContent"}).find('div', attrs={"id": "mw-content-text"}).find('div', attrs={"class": "mw-parser-output"})
        if not s:
            print('It leads to a dead end !')
            return
        p = []
        print('s: %s ' % s)
        #sys.exit(1)
        for child in s.children:
            print('child: %s ' % child)
            if child.name == 'p':
                p.append(child)
        if len(p) == 0:
            print('It leads to a dead end !')
            return
        a_all = []
        for child in p:
            for child1 in child:
                if child1.name == 'a':
                    a_all.append(child1)
        if len(a_all) == 0:
            print('It leads to a dead end !')
            return
        z = []
        for c in a_all:
            try:
                title=c["title"]
            except:
                title=None
            if not title:
                continue
            if not (title.startswith('Help:')) and (not title.startswith('Wikipedia:Citation needed')):
                try:
                    z.append(c["href"])
                except:
                    continue
            if len(z) == 0:
                print('It leads to a dead end !')
                return
            word = z[0].split('/')[2]


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('usage: ./roads_to_philosophy.py chaine-recherche')
        sys.exit(1)
    string_to_search = sys.argv[1]
    search_word(string_to_search)
