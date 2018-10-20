from django.shortcuts import render
from django.http import HttpResponse
import psycopg2

# Create your views here.
def index_fonction(request):
    return HttpResponse("Hello World'")

def day05_home(request):
    return render(request, 'day05_home.html')

def ex05_readme(request):
    rr = []
    rr.append(" python manage.py makemigrations ex05 ")
    rr.append(" python manage.py sqlmigrate ex05 0001")
    rr.append(" python manage.py migrate")
    rr.append(" python manage.py migrate --fake ex05 zero")
    rr.append(" python manage.py showmigrations")

    args = {'data': rr }
    return render(request, 'ex05/ex05_readme.html', args)

def ex05_populate(request):
    r = populate()
    args = {'data': r}
    return render(request, 'ex05/ex05_populate.html', args)

def ex05_display(request):
    r = display()
    error = r["error"]
    args = {'error': error, 'data': r["infos"]}
    return render(request, 'ex05/ex05_display.html', args)

def ex05_remove(request):
    r = remove(request)
    error = r["error"]
    args = {'error': error, 'data': r["infos"]}
    return render(request, 'ex05/ex05_remove.html', args)

def populate():
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
            m = Movies(
			   episode_nb=item[0],
			   title=item[1],
			   director=item[2],
			   producer=item[3],
			   release_date=item[4]
			)
            m.save()
            infos.append(item[1] + ": OK")
        except Exception as e:
            infos.append(item[1] + ": Not ok - reason: " + e.args[0])
            #break
    return infos

def display():
    returned_infos = {"error": "none", "infos": []}
    infos = []
    try:
        r = Movies.objects.all()

        for row in r:
            lr = (row.episode_nb, row.title, row.opening_crawl,row.director, row.producer, row.release_date)
            infos.append(lr)

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



def remove(request):
    returned_infos = {"error": "none", "infos": []}
    try:
        conn = psycopg2.connect(
            database='formationdjango',
			host='localhost',
			user='djangouser',
			password='secret'
			)

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
        #return HttpResponse("No data available")
        #return ["Not ok: " + str(e)]
        returned_infos["error"] = "yes"
        returned_infos["infos"] = ["Not ok:" + str(e)]
        return (returned_infos)


def remove(request):
    returned_infos = {"error": "none", "infos": []}
    try:

        if (request.method == "POST"):
            form = request.POST
            if "title" in form:
                m = Movies.objects.filter(episode_nb=int(form['title'][1:].replace('"', '')))
                m.delete()

        response = Movies.objects.all()

        infos = []
        for row in response:
            data = (row.title, row.episode_nb)
            infos.append(data)
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
