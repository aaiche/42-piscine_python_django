# coding : utf8

from django import forms
from django.contrib.auth import get_user_model
from .models import Tip

class InscriptionForm(forms.Form):
    username = forms.CharField(required = True)
    password = forms.CharField(
            required = True,
            widget=forms.PasswordInput,
            initial='',
    )
    verif_password = forms.CharField(
            required = True,
            widget=forms.PasswordInput,
            initial='',
    )

    def clean(self):
        User = get_user_model()
        form_data = self.cleaned_data
        unique = User.objects.filter(username=form_data['username'])
        if len(unique) > 0:
            self._errors['username'] = ["Le nom saisi est déjà utilisé"]
        if form_data['password'] != form_data['verif_password']:
            self._errors['password'] = ["mots de passe différents"]
        return form_data

class ConnexionForm(forms.Form):
    User = get_user_model()
    username = forms.CharField(required = True)
    password = forms.CharField(
            required = True,
            widget=forms.PasswordInput,
            initial='',
    )

class TipForm(forms.ModelForm):
    class Meta:
        model = Tip
        fields = ['contenu',]
