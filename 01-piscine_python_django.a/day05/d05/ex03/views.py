from django.shortcuts import render
from django.http import HttpResponse
import psycopg2
from .models import Movies

# Create your views here.
def index_fonction(request):
    return HttpResponse("Hello World'")

def day05_home(request):
    return render(request, 'day05_home.html')

def ex03_readme(request):
    #rr = init()
    rr = []
    rr.append(" python manage.py makemigrations ex03 ")
    rr.append(" python manage.py sqlmigrate ex03 0001")
    rr.append(" python manage.py migrate")
    rr.append(" python manage.py migrate --fake ex03 zero")
    rr.append(" python manage.py showmigrations")

    args = {'data': rr }
    return render(request, 'ex03/ex03_readme.html', args)

def ex03_populate(request):
    #rr = init()
    # ?? TBD ??
    r = populate()
    #args = {'returncode': r }
    #name = 'toto'
    #numbers = [1, 2, 3, 4, 5]

    #args = {'myName': name, 'numbers': r}
    args = {'data': r}
    return render(request, 'ex03/ex03_populate.html', args)

def ex03_display(request):
    r = display()
    args = {'returncode': r }
    name = 'toto'
    numbers = [1, 2, 3, 4, 5]
    error = r["error"]
    args = {'error': error, 'data': r["infos"]}
    return render(request, 'ex03/ex03_display.html', args)

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
