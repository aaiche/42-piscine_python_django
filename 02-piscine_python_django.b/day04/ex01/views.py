from django.shortcuts import render, HttpResponse
from .forms import MyForm

# Create your views here.

def django(request):
    return render(request, "ex01/django_inherit_from_base.html")

def affichage(request):
    return render(request, "ex01/affichage_inherit_from_base.html")

def templates(request):
    return render(request, "ex01/templates_inherit_from_base.html")
