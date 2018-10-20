from django.shortcuts import render
from django.http import HttpResponse
import psycopg2

# Create your views here.
def index_fonction(request):
    return HttpResponse("Hello World'")

def day05_home(request):
    return render(request, 'day05_home.html')

def ex00_home(request):
    r = init()
    args = {'returncode': r }
    return render(request, 'ex00/ex00_home.html', args)


def base(request):
    return render(request, 'base.html')


def init():
    try:
        conn = psycopg2.connect(
            database='formationdjango',
            host='localhost',
            user='djangouser',
            password='secret'
        )

        curr = conn.cursor()

        #curr.execute("""CREATE TABLE ex00_movies(
        curr.execute("""CREATE TABLE IF NOT EXISTS ex00_movies(
            title varchar(64) UNIQUE NOT NULL,
            episode_nb integer PRIMARY KEY,
            opening_crawl text,
            director varchar(32) NOT NULL,
            producer varchar(128) NOT NULL,
            release_date date NOT NULL
            )
            """)

        conn.commit()
        conn.close()
        #return HttpResponse("OK")
        return("OK")
    except Exception as e:
        #return HttpResponse(e)
        #return str("dsklsdlkl" + HttpResponse(e))
        return("Not Ok: " + str(e))


def OLDhome(request):
    numbers = [1, 2, 3, 4, 5]
    name = "Max Goodridge"

    args = {'myName': name, 'numbers': numbers}

    return render(request, 'accounts/home.html', args)
