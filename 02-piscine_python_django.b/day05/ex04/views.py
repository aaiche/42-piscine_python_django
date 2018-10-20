from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse
import psycopg2

# Create your views here.
def index_fonction(request):
    return HttpResponse("Hello World'")

def day05_home(request):
    return render(request, 'day05_home.html')

def ex04_home(request):
    rr = ex04_create_table()
    args = {'returncode': rr }
    return render(request, 'ex04/ex04_home.html', args)

def ex04_create_table():
    try:
        conn = psycopg2.connect(
            database='formationdjango',
            host='localhost',
            user='djangouser',
            password='secret'
        )
        curr = conn.cursor()
        curr.execute("""CREATE TABLE IF NOT EXISTS ex04_movies(
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
        return("OK")
    except Exception as e:
        return("Not Ok: " + str(e))


def ex04_populate(request):
    r = ex04_populate_table()
    args = {'data': r}
    return render(request, 'ex04/ex04_populate.html', args)

def ex04_populate_table():
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
                    INSERT INTO ex04_movies(episode_nb, title, director, producer, release_date) VALUES
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



def ex04_display(request):
    r = ex04_display_table()
    error = r["error"]
    args = {'error': error, 'data': r["infos"]}
    return render(request, 'ex04/ex04_display.html', args)


def ex04_display_table():
    returned_infos = {"error": "none", "infos": []}
    try:
        conn = psycopg2.connect(
            database='formationdjango',
            host='localhost',
            user='djangouser',
            password='secret'
            )
        curr = conn.cursor()
        curr.execute(""" SELECT * FROM ex04_movies """)
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
        returned_infos["error"] = "yes"
        returned_infos["infos"] = ["Not ok:" + str(e)]
        return (returned_infos)

def ex04_remove(request):
    r = ex04_remove_table(request)
    error = r["error"]
    args = {'error': error, 'data': r["infos"]}
    return render(request, 'ex04/ex04_remove.html', args)


def ex04_remove_table(request):
    returned_infos = {"error": "none", "infos": []}
    try:
        conn = psycopg2.connect(
            database='formationdjango',
			host='localhost',
			user='djangouser',
			password='secret'
			)


#    curr.execute(""" DELETE FROM members WHERE lastname LIKE 'Clapton'      """)

        curr = conn.cursor()
        if (request.method == "POST"):
            form = request.POST
            if "title" in form:
                curr.execute(" DELETE FROM ex04_movies WHERE episode_nb = %s", [int(form['title'][1:].replace('"', ''))])
                conn.commit()

        curr.execute(""" SELECT * FROM ex04_movies """)
        response = curr.fetchall()

        infos = []
        for row in response:
            data = (row[0], row[1])
            infos.append(data)
        conn.close()
        returned_infos["error"] = "none"
        returned_infos["infos"] = infos

        if infos == []:
            returned_infos["error"] = "empty"
            returned_infos["infos"] = "No data available"
            return (returned_infos)
        return (returned_infos)
    except Exception as e:
        returned_infos["error"] = "yes"
        returned_infos["infos"] = ["Not ok:" + str(e)]
        return (returned_infos)
