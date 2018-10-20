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
# Si erreur: NOTE: je n ai pas ces erreurs a la 1ere pisc.
#   e1r12p13% pip3 install virtualenv
#           Collecting virtualenv
#           Using cached https://files.pythonhosted.org/packages/b6/30/96a02b2287098b23b875bc8c2f58071c35d2efe84f747b64d523721dc2b5/virtualenv-16.0.0-py2.py3-none-any.whl
#           Installing collected packages: virtualenv
#           Could not install packages due to an EnvironmentError: [Errno 13] Permission denied: '/lib'
#           Consider using the `--user` option or check the permissions.
# alors:
#   e1r12p13% pip3 install virtualenv --user
#       Collecting virtualenv
#           Using cached https://files.pythonhosted.org/packages/b6/30/96a02b2287098b23b875bc8c2f58071c35d2efe84f747b64d523721dc2b5/virtualenv-16.0.0-py2.py3-none-any.whl
#           Installing collected packages: virtualenv
#               The script virtualenv is installed in '/Users/aaiche/Library/Python/3.7/bin' which is not on PATH.
#               Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
#       Successfully installed virtualenv-16.0.0
#
#creer nouvel environnement
#	virtualenv monNouveauEnvVirtuel
#       si erreur : retirer ce qu il dans ~/.pydistutils.cfg
#
#activer le nouvel environnement
#	source monNouveauEnvVirtuel/bin/activate
#
#installer les packages requis cf. requirements.txt
#   pip install requests
#   pip install dewiki
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
#   e) (myNewEnv) e1r12p13% python3 request_wikipedia.py "chocolatine"
#
#   f) (myNewEnv) e1r12p13% ll -rtl
#       ...
#       chocolatine.wiki
#       ...
#       
"""
    Framework Django D01 - 42
    Created on:
    Author
"""

""" 
    on importe le module sys
"""

""" ces packages existent deja ds l env cree """
import sys
import json
""" ces packages doivent etre installes par pip """
import requests # requetes http
import dewiki # parser

""" 
    global variables
"""

def send_http_request(url, s_to_search):
    payload = {
            'action':'query', 
            'titles':s_to_search, 
            'prop':'revisions',
            'rvprop':'content',
            'redirects':'true',
            'format':'json'
    }
    r = requests.get(url,params=payload)
    # Faire l equivalent de cette commande:
    #print(r.status_code)
    #print(r.url)
    #       https://fr.wikipedia.org/w/api.php?action=query&titles=chocolatine&prop=revisions&rvprop=content&format=json
    #   curl "https://fr.wikipedia.org/w/api.php?action=query&titles=chocolatine&prop=revisions&rvprop=content&format=json" | jq  '.'
    #   
    # action: query 
    # titles: pages ayant pour titre 'chocolatine'
    # prop:revisions propriete inclure les revisions
    # prop:revisions&rvprop=content: lire le contenu
    #       exple:
    #           curl "https://fr.wikipedia.org/w/api.php?action=query&titles=chocolatine&prop=revisions&rvprop=content&format=json" | jq  '.'
    #               ...
    #               "pages": {
    #                   "908647": {
    #                       "pageid": 908647,
    #                       "ns": 0,
    #                       "title": "Chocolatine",
    #                       "revisions": [
    #                           {
    #                               "contentformat": "text/x-wiki",
    #                               "contentmodel": "wikitext",
    #                               "*": "#REDIRECT[[Pain au chocolat]]"
    #                           }
    #                       ]
    #   Ci-dessus il y une redirection : donc on fait e1r12p13% curl "https://fr.wikipedia.org/w/api.php?action=query&titles=chocolatine&prop=revisions&rvprop=content&redirects&format=json" | jq  '.'
    #

    #sys.exit(1)
    #print(r.status_code)

    #TBD verifier que la page n est pas redirige avec le header ---> #print(r.headers)
    #print(r.content)
    if r.status_code == 200:
        # reponse http == ok
        if not r.text:
            print("verifier r.text pas le temps %s" % r.text)
            sys.exit(1)
        #res = r.json()
        #print("debug : res=", res)

        """
        res = json.loads(r.text)
        #print(res)
        pages = res['query']['pages']

        for page_id in pages.keys():
            print(page_id)
            for page in page_id[pa
            sys.exit(1)
            """
        #https://github.com/ajouanna/Piscine_Django_Python/blob/master/D03/ex02/request_wikipedia.py
        # parcourir le resultat json
        res = r.json()
        #print("debug : res=", res)
        if res.get('query'):
            #print('debug : query trouve')
            query = res['query']
            if query.get('pages'):
                pages = query['pages']
                #print('debug : pages trouve')
                txt = ""
                for pageid in pages:
                    page = pages[pageid]
                    if page.get('revisions'):
                        revisions = page['revisions']
                        #print('debug : revisions trouve ',revisions)
                        if revisions[0].get('*'):
                            #print('debug : contentu trouve ',revisions[0]['*'] )
                            txt += revisions[0]['*'] + "\n" 

                            txt = dewiki.from_string(txt)
        #write_in_file(req, txt)
        filename = s_to_search.replace(" ", "_") + ".wiki"
        f = open(filename, "w")
        f.write(txt)
        f.close()

    else:
        # selon le cas :
            # soit erreur
            # soit page redirige, etc....
        print("http request status is %s" % r.status)
        print("TBD analyser le code retour: ce n est pas forcement une erreur")
        sys.exit(1)



def main(s):
    """
    """
    url = 'https://fr.wikipedia.org/w/api.php'
    #print("s: %s" % s)
    send_http_request(url, s)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('usage: ./request_wikipedia.py chaine_recherche')
        sys.exit(1)

    string_to_search = sys.argv[1]

    main(string_to_search)
