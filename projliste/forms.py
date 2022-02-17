from django import forms
from captcha.fields import ReCaptchaField
class NameForm(forms.Form):
    titre = forms.CharField(label='Titre', max_length=100)
    desc = forms.CharField(label='Desc', max_length=100)
    donneur = forms.CharField(label='donneur', max_length=100)
    captcha=ReCaptchaField()
