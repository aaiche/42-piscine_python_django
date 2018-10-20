7
from django.shortcuts import render
from django.http import HttpResponse
import psycopg2

# Create your views here.
def index_fonction(request):
    return HttpResponse("Hello World'")

def day05_home(request):
    return render(request, 'day05_home.html')

def ex02_home(request):
    rr = init()
    args = {'returncode': rr }
    return render(request, 'ex02/ex02_home.html', args)

def ex02_populate(request):
    r = populate()
    #args = {'returncode': r }
    #name = 'toto'
    #numbers = [1, 2, 3, 4, 5]

    #args = {'myName': name, 'numbers': r}
    args = {'numbers': r}
    return render(request, 'ex02/ex02_populate.html', args)

def ex02_display(request):
    r = display()
    args = {'returncode': r }
    name = 'toto'
    numbers = [1, 2, 3, 4, 5]
    error = r["error"]
    args = {'error': error, 'data': r["infos"]}
    return render(request, 'ex02/ex02_display.html', args)


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
        curr.execute("""CREATE TABLE IF NOT EXISTS ex02_movies(
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

def populate():
    try:
        conn = psycopg2.connect(
            database='formationdjango',
            host='localhost',
            user='djangouser',
            password='secret'
            )
        curr = conn.cursor()

        ls = [
            (1, "The Phantom Menace", "George Lucas", "Rick McCallum", "1999-05-19"),
            (2, "Attack of the Clones", "George Lucas", "Rick McCallum", "2002-05-16"),
            (3, "Revenge of the Sith",  "George Lucas", "Rick McCallum", "2005-05-19"),
            (4, "A New Hope", "George Lucas", "GaryKurtz, Rick McCallum", "1977-05-25"),
            (5, "The Empire Strikes Back", "Irvin Kershner", "Gary Kutz, Rick McCallum", "1980-05-17"),
            (6, "Return of the Jedi", "Richard Marquand", "Howard G. Kazanjian, George Lucas, Rick McCallum","1983-05-25"),
            (7, "The Force Awakens", "J. J. Abrams", "Kathleen Kennedy, J. J. Abrams, Bryan Burk", "2015-12-11")
        ]
        infos = []
        for item in ls:
            try:
                curr.execute("""
                    INSERT INTO ex02_movies(episode_nb, title, director, producer, release_date) VALUES
                    (%s,%s,%s,%s,%s)""", (item[0], item[1], item[2], item[3], item[4]))
                conn.commit()
                infos.append(item[1] + ": OK")
            except Exception as e:
                infos.append(item[1] + ": Not ok - reason: " + e.args[0])
                #break

        conn.commit()
        conn.close()

        return infos

    except Exception as e:
        return(["Not Ok:   " + str(e)])



def display():
    returned_infos = {"error": "none", "infos": []}
    try:
        conn = psycopg2.connect(
            database='formationdjango',
            host='localhost',
            user='djangouser',
            password='secret'
            )

        curr = conn.cursor()

        curr.execute(""" SELECT * FROM ex02_movies """)
        response = curr.fetchall()
        infos = []
        for row in response:
            infos.append(row)
        conn.close()
        returned_infos["error"] = "none"
        returned_infos["infos"] = infos
        if infos == []:
            returned_infos["error"] = "empty"
            returned_infos["infos"] = "No data available"
            return (returned_infos)
        return (returned_infos)

    except Exception as e:
        #return HttpResponse("No data available")
        #return ["Not ok: " + str(e)]
        returned_infos["error"] = "yes"
        returned_infos["infos"] = ["Not ok:" + str(e)]
        return (returned_infos)
