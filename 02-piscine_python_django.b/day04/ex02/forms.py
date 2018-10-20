from django import forms

"""
    classe MyForm qui hereite de Form
        on definit 2 attributs : email de type EmailField et name de type CharField
        on a definit 2 champs dans le formulaire: un champ email et un champ texte
        True: pour dire a django que ces 2 sont necessaires a la validation du formulaire
"""
class MyForm(forms.Form):
    juste_du_texte = forms.CharField(required = True)


"""
class MyForm(forms.Form):
    email = forms.EmailField(required = True)
    name = forms.CharField(required = True)
"""
