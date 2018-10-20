from django.shortcuts import render
#from .models import Movies
from django.http import HttpResponse

# Create your views here.

def day05_home(request):
    return render(request, 'day05_home.html')

def ex01_home(request):
    rr = ex01_create_models()
    r = "ex01/models.py:\n" + rr
    args = {'returncode': r }
    return render(request, 'ex01/ex01_home.html', args)

def ex01_create_models():
    with open('ex01/models.py', 'r') as content_file:
        content = content_file.read()
    return(content)
