from django import forms
# from django.core import validators

from AppTwo import models

class UserForm(forms.ModelForm):
    class Meta:
        model = models.User
        fields = '__all__'
