from django.shortcuts import render
from django.http import HttpResponse
from .form import MyForm
import datetime
from django.utils import timezone
from django.conf import settings
# Create your views here.

def index(request):
    lst = list()
    now = datetime.datetime.now().strftime('%H:%M:%S %d-%m-%Y')

    if (request.method == 'POST'):
        form = MyForm(request.POST)
        if form.is_valid():
            with open(settings.MY_WAY, 'a') as f2:
                f2.write(now + " " + form.cleaned_data['text'] + "\n")

    form = MyForm()

    with open(settings.MY_WAY, 'r') as f:
        for line in f:
            lst.append(line)

    return render(request, "ex02/index.html", {'form' : form, 'liste' : lst})

