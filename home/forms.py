from django import forms
from django.forms import widgets
from . models import Marketers


class userform(forms.ModelForm):
    class  Meta:
        model = Marketers
        widgets={
            'password': forms.PasswordInput()
        }
      