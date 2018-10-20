from django.shortcuts import render, HttpResponse
from .forms import MyForm
import datetime
import os.path
from django.conf import settings


def withform(request):
    log_file = getattr(settings, "HISTORY_FILE", None)          # il est positionne dans settings

    historique = []
    if os.path.isfile(log_file) :       # on ne lit que si le fichier existe
        with open(log_file) as f:
            historique = f.readlines()

    if (request.method == 'POST'):      # Si la requete est de type POST, cela veut dire que l on a envoye des donnes
        form = MyForm(request.POST)     # on instancie un nouveau formulaire A L AIDE Des DONNEES RECUES par le biais de cette requete POST. Puis le formulaire form contiendra les donnees qui ont ete envoyees
        if form.is_valid():
            juste_du_texte = str(datetime.datetime.now()) + ': ' + form.cleaned_data['juste_du_texte']
            form.cleaned_data['juste_du_texte'] = ''
            f = open(log_file, 'a')
            f.write(juste_du_texte + '\n') # ecrire le message dans le fichier
            f.close()

            historique.append(juste_du_texte)
            #return HttpResponse("You correctly filled the form!\nYou're %s and your email is %s" % (form.cleaned_data['name'], form.cleaned_data['email']))
    #else:
        # on demande la page et ici on genere un formulaire vide a partir de ma classe
        #form = MyForm()
    #return render(request, "ex02/form.html", {'form' : form, 'historique': [1, 2, 3, 4, 4, 5, 6, 7, 8, 9, 10]}) # on retourne la page avec le formulaire ci-dessus
    form = MyForm()
    return render(request, "ex02/form.html", {'form' : form, 'historique': historique}) # on retourne la page avec le formulaire ci-dessus

"""
class MyForm(forms.Form):
    email = forms.EmailField(required = True)
    name = forms.CharField(required = True)

class MyForm(forms.Form):
    text = forms.CharField(required = True)

"""
