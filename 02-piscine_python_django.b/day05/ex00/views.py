from django.shortcuts import render
#from .models import Members
from django.http import HttpResponse

"""
    on importe le module psycopg2
    module qui fait l interface avec postgresql
"""
import psycopg2

# Create your views here.

def day05_home(request):
    return render(request, 'day05_home.html')

def ex00_home(request):
    r = ex00_init_create_table()
    args = {'returncode': r }
    return render(request, 'ex00/ex00_home.html', args)

def ex00_init_create_table():
    try:
        # pour se connecter a la bdd
        # ?? TBD : gerer l erreur
        conn = psycopg2.connect(
            database='formationdjango',
            host='localhost',
            user='djangouser',
            password='secret'
        )

        # le cursor: var nous permettre d interagir avec postgresql
        curr = conn.cursor()

        # executer des cmdes sql
        curr.execute("""CREATE TABLE IF NOT EXISTS ex00_movies(
            title varchar(64) UNIQUE NOT NULL,
            episode_nb integer PRIMARY KEY,
            opening_crawl text,
            director varchar(32) NOT NULL,
            producer varchar(128) NOT NULL,
            release_date date NOT NULL
            )
            """)

        # permet d appliquer la cmde precedente
        conn.commit()

        # puis on fermer
        conn.close()
        #return HttpResponse("OK")
        return("OK")
    except Exception as e:
        #return HttpResponse(e)
        #return str("dsklsdlkl" + HttpResponse(e))
        return("Not Ok: " + str(e))
