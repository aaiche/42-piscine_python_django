from django.shortcuts import render
from django.http import HttpResponse
"""
    on importe le module psycopg2
    module qui fait l interface avec postgresql
"""
import psycopg2
# Create your views here.



def day05_home(request):
    return render(request, 'day05_home.html')

def ex02_init(request):
    rr = ex02_init_create_table()
    args = {'returncode': rr }
    return render(request, 'ex02/ex02_home.html', args)

def ex02_populate(request):
    r = ex02_populate_table()
    #args = {'returncode': r }
    #name = 'toto'
    #numbers = [1, 2, 3, 4, 5]

    #args = {'myName': name, 'numbers': r}
    args = {'numbers': r}
    return render(request, 'ex02/ex02_populate.html', args)

def ex02_display(request):
    r = ex02_display_table()
    args = {'returncode': r }
    name = 'toto'
    numbers = [1, 2, 3, 4, 5]
    error = r["error"]
    args = {'error': error, 'data': r["infos"]}
    return render(request, 'ex02/ex02_display.html', args)

def ex02_display_table():
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
        episodes_list = []
        for row in response:
            episodes_list.append(row)
        conn.close()
        returned_infos["error"] = "none"
        returned_infos["infos"] = episodes_list
        if episodes_list == []:
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


def ex02_init_create_table():
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
        curr.execute("""CREATE TABLE IF NOT EXISTS ex02_movies(
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

def ex02_populate_table():
    try:
        conn = psycopg2.connect(
            database='formationdjango',
            host='localhost',
            user='djangouser',
            password='secret'
        )

        curr = conn.cursor()

        episodes_list = [
            (1, "The Phantom Menace", "George Lucas", "Rick McCallum", "1999-05-19"),
            (2, "Attack of the Clones", "George Lucas", "Rick McCallum", "2002-05-16"),
            (3, "Revenge of the Sith",  "George Lucas", "Rick McCallum", "2005-05-19"),
            (4, "A New Hope", "George Lucas", "GaryKurtz, Rick McCallum", "1977-05-25"),
            (5, "The Empire Strikes Back", "Irvin Kershner", "Gary Kutz, Rick McCallum", "1980-05-17"),
            (6, "Return of the Jedi", "Richard Marquand", "Howard G. Kazanjian, George Lucas, Rick McCallum","1983-05-25"),
            (7, "The Force Awakens", "J. J. Abrams", "Kathleen Kennedy, J. J. Abrams, Bryan Burk", "2015-12-11")
        ]
        episodes_insert_status = []

        for item in episodes_list:
            try:
                curr.execute("""
                    INSERT INTO ex02_movies(episode_nb, title, director, producer, release_date) VALUES
                    (%s, %s, %s, %s, %s)
                    """,
                    (item[0], item[1], item[2], item[3], item[4])
                )
                conn.commit()
                episodes_insert_status.append(item[1] + ": OK")
            except Exception as e:
                episodes_insert_status.append(item[1] + ": Not ok - reason: " + e.args[0])
                #break

        conn.commit()
        conn.close()

        return episodes_insert_status

    except Exception as e:
        return(["Not Ok:   " + str(e)])
