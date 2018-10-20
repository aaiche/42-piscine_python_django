from django.shortcuts import render, HttpResponse
from .forms import MyForm

# Create your views here.
"""
def myEx00(request):
    return HttpResponse("MY NEdsdasdassadassddsdsW APP.")
"""

def myEx00WithTemplate(request):
    return render(request, "ex00/index.html")

"""
def base(request):
    return render(request, "ex00/base.html")

def inherit(request):
    return render(request, "ex00/inherit.html")

def context_example(request):
    return render(request, "ex00/context.html", {'name': 'Bob'})

def for_eample(request):
    return render(request, "ex00/for.html", {'numbers': [1, 2, 3, 4, 4, 5, 6, 7, 8, 9, 10]})

def if_eample(request):
    return render(request, "ex00/if.html", {'numbers': [1, 2, 3, 4, 4, 5, 6, 7, 8, 9, 10]})

def include_example(request):
    return render(request, "ex00/include.html", {'numbers': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]})


def withform(request):
    if (request.method == 'POST'):      # Si la requete est de type POST, cela veut dire que l on a envoye des donnes
        form = MyForm(request.POST)     # on instancie un nouveau formulaire A L AIDE Des DONNEES RECUES par le biais de cette requete POST. Puis le formulaire form contiendra les donnees qui ont ete envoyees
        if form.is_valid():
            return HttpResponse("You correctly filled the form!\nYou're %s and your email is %s" % (form.cleaned_data['name'], form.cleaned_data['email']))
    else:
        # on demande la page et ici on genere un formulaire vide a partir de ma classe
        form = MyForm()
    return render(request, "ex00/form.html", {'form' : form}) # on retourne la page avec le formulaire ci-dessus
"""
