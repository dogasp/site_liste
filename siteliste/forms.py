from django import forms

class NameForm(forms.Form):
    titre = forms.CharField(label='Titre', max_length=100)
    desc = forms.CharField(label='Desc', max_length=100)

