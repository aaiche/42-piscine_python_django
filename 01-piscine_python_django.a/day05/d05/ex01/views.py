
from django.shortcuts import render
from django.http import HttpResponse
import psycopg2

# Create your views here.
def index_fonction(request):
    return HttpResponse("Hello World'")

def day05_home(request):
    return render(request, 'day05_home.html')

def ex01_home(request):
    rr = models()
    r = "ex01/models.py:\n" + rr
    args = {'returncode': r }
    return render(request, 'ex01/ex01_home.html', args)


def base(request):
    return render(request, 'base.html')


def models():
    with open('ex01/models.py', 'r') as content_file:
        content = content_file.read()
    return(content)



def OLDhome(request):
    numbers = [1, 2, 3, 4, 5]
    name = "Max Goodridge"

    args = {'myName': name, 'numbers': numbers}

    return render(request, 'accounts/home.html', args)
