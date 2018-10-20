from django.shortcuts import render
from django.http import HttpResponse
from .models import Movies


def day05_home(request):
    return render(request, 'day05_home.html')

def ex03_readme(request):
    #rr = init()
    rr = []
    rr.append(" python manage.py makemigrations ex03 ")
    rr.append(" python manage.py sqlmigrate ex03 0001")
    rr.append(" python manage.py migrate ex03")
    rr.append(" python manage.py migrate --fake ex03 zero")
    rr.append(" python manage.py showmigrations")

    args = {'data': rr }
    return render(request, 'ex03/ex03_readme.html', args)

def ex03_populate(request):
    r = ex03_populate_table()
    print(r)
    args = {'data': r}
    return render(request, 'ex03/ex03_populate.html', args)


def ex03_populate_table():
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
            m = Movies(
			   episode_nb = item[0],
			   title = item[1],
			   director = item[2],
			   producer = item[3],
			   release_date = item[4]
			)
            m.save()
            episodes_insert_status.append(item[1] + ": OK")
        except Exception as e:
            episodes_insert_status.append(item[1] + ": Not ok - reason: " + e.args[0])
            #break
    return episodes_insert_status



def ex03_display(request):
    r = ex03_display_table()
    error = r["error"]
    args = {'error': error, 'data': r["infos"]}
    return render(request, 'ex03/ex03_display.html', args)



def ex03_display_table():
    returned_infos = {"error": "none", "infos": []}
    episodes_list = []
    try:
        r = Movies.objects.all()

        for row in r:
            list_r = (row.title, row.episode_nb, row.opening_crawl, row.director, row.producer, row.release_date)
            #print(row.title)
            #print(row.opening_crawl)
            episodes_list.append(list_r)

        returned_infos["error"] = "none"
        returned_infos["infos"] = episodes_list
        if episodes_list == []:
            returned_infos["error"] = "empty"
            returned_infos["infos"] = "No data available"
            return (returned_infos)
        return (returned_infos)
    except Exception as e:
        returned_infos["error"] = "yes"
        returned_infos["infos"] = ["Not ok:" + str(e)]
        return (returned_infos)
