from django.shortcuts import render
from django.http import HttpResponse
from .forms import MyForm

import psycopg2

# Create your views here.
def index_fonction(request):
    return HttpResponse("Hello World'")

def day05_home(request):
    return render(request, 'day05_home.html')

def ex06_home(request):
    rr = ex06_create_table()
    args = {'returncode': rr }
    return render(request, 'ex06/ex06_home.html', args)

def ex06_create_table():
    try:
        conn = psycopg2.connect(
            database='formationdjango',
            host='localhost',
            user='djangouser',
            password='secret'
        )
        curr = conn.cursor()
        curr.execute("""CREATE TABLE IF NOT EXISTS ex06_movies(
            title varchar(64) UNIQUE NOT NULL,
            episode_nb integer PRIMARY KEY,
            opening_crawl text,
            director varchar(32) NOT NULL,
            producer varchar(128) NOT NULL,
            release_date date NOT NULL,
            created timestamp DEFAULT(now()),
            updated timestamp DEFAULT(now())
            )
            """)

        curr.execute(""" CREATE OR REPLACE FUNCTION update_changetimestamp_column()
            RETURNS TRIGGER AS $$
            BEGIN
            NEW.updated = now();
            NEW.created = OLD.created;
            RETURN NEW;
            END;
            $$ language 'plpgsql';

            CREATE TRIGGER update_films_changetimestamp BEFORE UPDATE
            ON ex06_movies FOR EACH ROW EXECUTE PROCEDURE
            update_changetimestamp_column();
            """)

        conn.commit()
        conn.close()
        return("OK")
    except Exception as e:
        return("Not Ok: " + str(e))


# https://stackoverflow.com/questions/1035980/update-timestamp-when-row-is-updated-in-postgresql?rq=1
# Create a function that updates the changetimestamp column of a table like so:
#    CREATE OR REPLACE FUNCTION update_changetimestamp_column()
#    RETURNS TRIGGER AS $$
#    BEGIN
#       NEW.changetimestamp = now();
#       RETURN NEW;
#    END;
#    $$ language 'plpgsql';
#
# Create a trigger on the table that calls the update_changetimestamp_column() function whenever an update occurs like so:
#    CREATE TRIGGER update_ab_changetimestamp BEFORE UPDATE
#    ON ab FOR EACH ROW EXECUTE PROCEDURE
#    update_changetimestamp_column();

# List triggers:
# ----------------
# SELECT event_object_table
#      ,trigger_name
#      ,event_manipulation
#      ,action_statement
#      ,action_timing
# FROM  information_schema.triggers
# WHERE event_object_table = 'ex06_movies'
# ORDER BY event_object_table
#     ,event_manipulation
#
# Drop trigger:
# ---------------
# DROP TRIGGER IF EXISTS update_films_changetimestamp on ex06_movies;
#
# List triggers:
# ----------------
# select relname as table_with_trigger
# from pg_class
# where pg_class.oid in (
#        select tgrelid
#        from pg_trigger
#        )


def ex06_populate(request):
    r = ex06_populate_table()
    args = {'data': r}
    return render(request, 'ex06/ex06_populate.html', args)

def ex06_populate_table():
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
                    INSERT INTO ex06_movies(episode_nb, title, director, producer, release_date) VALUES
                    (%s,%s,%s,%s,%s)""", (item[0], item[1], item[2], item[3], item[4]))
                conn.commit()
                infos.append(item[1] + ": OK")
            except Exception as e:
                infos.append(item[1] + ": Not ok - reason: " + e.args[0])

        conn.commit()
        conn.close()
        return infos
    except Exception as e:
        return(["Not Ok:   " + str(e)])



def ex06_display(request):
    r = ex06_display_table()
    error = r["error"]
    args = {'error': error, 'data': r["infos"]}
    return render(request, 'ex06/ex06_display.html', args)


def ex06_display_table():
    returned_infos = {"error": "none", "infos": []}
    try:
        conn = psycopg2.connect(
            database='formationdjango',
            host='localhost',
            user='djangouser',
            password='secret'
            )
        curr = conn.cursor()
        curr.execute(""" SELECT * FROM ex06_movies """)
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

def ex06_update(request):
    r = ex06_update_table(request)
    error = r["error"]
    args = {'error': error, 'data': r["infos"]}
    return render(request, 'ex06/ex06_update.html', args)


def ex06_update_table(request):
    returned_infos = {"error": "none", "infos": []}
    try:
        conn = psycopg2.connect(
            database='formationdjango',
			host='localhost',
			user='djangouser',
			password='secret'
			)
        #   curr.execute(""" DELETE FROM members WHERE lastname LIKE 'Clapton'      """)
        curr = conn.cursor()
        if (request.method == "POST"):
            form = request.POST
            if "title" in form:
                if "opening_crawl" in form:
                    if form['opening_crawl']:
                        curr.execute(" UPDATE ex06_movies SET opening_crawl = %s  WHERE episode_nb = %s", (form['opening_crawl'], form['title'] ))
                        #new_title = form['title'].split(':', 1)[0]
                        #curr.execute(" UPDATE ex06_movies SET opening_crawl = %s  WHERE episode_nb = %s", (form['opening_crawl'], new_title ))
                        conn.commit()


        curr.execute(""" SELECT * FROM ex06_movies ORDER BY episode_nb """)
        response = curr.fetchall()

        infos = []
        for row in response:
            data = (row[0], row[1], row[2], row[6], row[7])
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
