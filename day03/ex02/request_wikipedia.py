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
#installer les packages requis cf. requirements.txt
#   pip install requests
#   pip install dewiki
# 
# 
#preferer python3 a  #!/usr/bin/python3 car on utilise celui de la virtuelle
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
    payload = {'action':'query', 'titles':s_to_search, 'prop':'revisions','rvprop':'content','format':'json'}
    r = requests.get(url,params=payload)
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
