"""
from django.shortcuts import render

# Create your views here.
"""

from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("encore une journee de m... que de frustrations...")

def withtemplate(request):
    return render(request, 'ex00/index.html')

