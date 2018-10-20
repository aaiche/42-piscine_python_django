from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from .models import Movies

def day05_home(request):
    return render(request, 'day05_home.html')

def ex07_readme(request):
    rr = []
    rr.append(" python manage.py makemigrations ex07 ")
    rr.append(" python manage.py sqlmigrate ex07 0001")
    rr.append(" python manage.py migrate ex07")
    rr.append(" python manage.py migrate --fake ex07 zero")
    rr.append(" python manage.py showmigrations")

    args = {'data': rr }
    return render(request, 'ex07/ex07_readme.html', args)

def ex07_populate(request):
    r = ex07_populate_table()
    print(r)
    args = {'data': r}
    return render(request, 'ex07/ex07_populate.html', args)

def ex07_populate_table():
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
    return episodes_insert_status

def ex07_display(request):
    r = ex07_display_table()
    error = r["error"]
    args = {'error': error, 'data': r["infos"]}
    return render(request, 'ex07/ex07_display.html', args)

def ex07_display_table():
    returned_infos = {"error": "none", "infos": []}
    infos = []
    print('toto toto toto')

    try:
        r = Movies.objects.all()
        for row in r:
            lr = (row.title, row.episode_nb, row.opening_crawl, row.director, row.producer, row.release_date, row.created, row.updated)
            print(row.title)
            print(row.opening_crawl)
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
        returned_infos["infos"] = ["Not ooooook:" + str(e)]
        return (returned_infos)

def ex07_update(request):
    r = ex07_update_episode(request)
    error = r["error"]
    args = {'error': error, 'data': r["infos"]}
    return render(request, 'ex07/ex07_update.html', args)

def ex07_update_episode(request):
    returned_infos = {"error": "none", "infos": []}
    try:
        if (request.method == "POST"):
            form = request.POST
            if "title" in form:
                if "opening_crawl" in form:
                    if form['opening_crawl']:
                        #print('rec. title ===> %s ' % form['title'])
                        #print('rec. title ===> %s ' % form['title'][1:].replace(':', ''))
                        #rest = form['title'].split(':', 1)[0]
                        #print('rec. title ===> %s ' % rest)
                        #print('rec. opening_crawl ===> %s ' % form['opening_crawl'])
                        new_title = form['title'].split(':', 1)[0]
                        #m = Movies.objects.get(episode_nb=int(form['title']))
                        m = Movies.objects.get(episode_nb=int(new_title))

                        # NE FONCTIONNE PAS MyModel.objects.get(name=name).update(field=value)
                        #m.update(updated=datetime.now)
                        #m.update(opening_crawl='TOTO')
                        m.opening_crawl = form['opening_crawl']
                        #m.current = datetime.now()
                        #print('old opening_crawl ===> %s ' % m.opening_crawl)
                        #m.opening_crawl = form['opening_crawl']
                        #curr.execute(" UPDATE ex06_movies SET opening_crawl = %s  WHERE episode_nb = %s", (form['opening_crawl'], form['title'] ))
                        m.save()

        response = Movies.objects.all()

        infos = []
        for row in response:
            data = (row.title, row.episode_nb, row.opening_crawl, row.created, row.updated)
            infos.append(data)
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
