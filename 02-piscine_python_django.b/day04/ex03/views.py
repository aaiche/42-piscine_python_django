from django.shortcuts import render, HttpResponse

def tableau(request):
    return render(request, "ex03/base.html", {'numbers': list(range(0, 250, 5))})
