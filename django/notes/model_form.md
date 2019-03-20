a model form is a form connected to a model and can pass user input to the model objects   
in forms.py
```py
from django import forms

from AppTwo import models

class UserForm(forms.ModelForm):
    class Meta:
        model = models.User
        fields = '__all__'

```
in views.py   
```py
from django.shortcuts import render
from django.http import HttpResponseRedirect

from AppTwo.models import User
from AppTwo import forms
# Create your views here.
def index(request):
    return render(request, 'AppTwo/index.html')

def help(request):
    dict = {'something': 'Help Page'}
    return render(request, 'AppTwo/help.html', context=dict)

def users(request):
    dict = {'users': User.objects.all()}
    return render(request, 'AppTwo/users.html', context=dict)

def user_form_view(request):
    if request.method =='POST':
        form = forms.UserForm(request.POST)
        if form.is_valid():
            form.save()
            return index(request)
            # return HttpResponseRedirect('')
    else:
        form = forms.UserForm()
    return render(request, 'AppTwo/form_page.html', {'form': form})
```
in template: form_page.html   
```html
<!DOCTYPE html>
<html lang="en" dir="ltr">
    <head>
        <meta charset="utf-8">
        <title>Register</title>
        <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
    </head>
    <body>
        <div class="container">
            <h1>Register</h1>
            <form method="post">
                {{ form.as_p }}
                {% csrf_token %}
                <input type="submit" class="btn btn-primary" value="Sign Up">
            </form>
        </div>
    </body>
</html>

```
then change the urls.py routes
