in models.py
```py
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class UserProfileInfo(models.Model):
    # create realtionship
    user = models.OneToOneField(User,on_delete=models.CASCADE)

    portfolio = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_pics', blank=True)

    def __str__(self):
        return self.user.username
```
create a new 'profile_pics' folder under the media folder   
register this model to admin, in admin.py
```py
from django.contrib import admin

from basic_app.models import UserProfileInfo
# Register your models here.
admin.site.register(UserProfileInfo)
```
under app dir, create a forms.py
```py
from django import forms
from from django.contrib.auth.models import User
from basic_app.models import UserProfileInfo

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username', 'email', 'password')

class UserProfileForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('portfolio', 'picture')
```
migrate
```shell
python manage.py migrate
```
```shell
python manage.py makemigrations basic_app
```
```shell
python manage.py migrate
```
