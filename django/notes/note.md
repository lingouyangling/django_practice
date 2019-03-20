# setup
## create a new project
cd to a dir and
```shell
django-admin startproject first_project
```
## test installation
cd to the the project dir
```shell
python manage.py runserver
```
then open browser and go to localhost:8000
## create a new app
cd to the the project dir
```shell
python manage.py startapp first_app
```
## add the app to the project
open settings.py under project dir   
find the list INSTALLED_APPS, and add 'first_app' to it   
# view and urls
## create a simple view
### go to views.py under the first_app dir   
### import HttpResponse
```py
from django.http import HttpResponse
```
### create a new index() function   
```py
def index(request):
    return HttpResponse("Hello World")
```
## route urls to the view
go to urls.py under the project dir   
import the view
```py
from first_project import views
```
find the list urlpatterns, and add
```py
path('', views.index, name='index')
```
go to the browser and see the new change
## url mapping
go to the urls.py under project dir, use include() to map urls   
```py
# ...
from django.urls import path, include, re_path
urlpatterns = [
    # ...
    re_path(r'^first_app/', include('first_app.urls')),
]
# ...
```
this means users visit any url that includes 'domain/first_app/' will be processed by url rules in the urls.py under the app dir   
create a urls.py under the app dir   
```py
from django.urls import path, include, re_path
from first_app import views

urlpatterns =[
    re_path(r'^$', views.index, name='index'),
]
```
# templates
create a templates dir under the top lever dir   
create a sub dir under the template dir per each app   
go to the setting.py, create a variable for template path
```py
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')
```
add the variable to the TEMPLATES settings
```py
TEMPLATES = [
    # ...
    'DIRS': [
        TEMPLATES_DIR,
    ],
    #...
]
```
put html file into templates sub dir
```html
<!DOCTYPE html>
<html lang="en" dir="ltr">
    <head>
        <meta charset="utf-8">
        <title>First App</title>
    </head>
    <body>
        <h1>Hello this is index.html!</h1>
        {{ insert_me }}
    </body>
</html>
```
edit the function in the views.py
```py
def index(request):
    my_dict = {'insert_me':'hello, i am from views.py'}
    return render(request, 'first_app/index.html', context=my_dict)
```
# static
create a static dir under the top lever dir   
create a images dir under the static dir    
put some jpg file in the image dir   
go to the setting.py, create a variable for template path   
```py
STATIC_DIR = os.path.join(BASE_DIR, 'static')
```
edit the static setting   
```py
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    STATIC_DIR,
]
```
to enable visiting the jpg, go to the urls.py   
import two things   
and add a '+ static()' statement after the urlpatterns
```py
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # re_path('^$', views.index, name='index'),
    # path('admin/', admin.site.urls),
    # re_path(r'^first_app/', include('first_app.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

```
## add static file to template
go to index.html under template
add load tag under !doctype statement
```html
<!DOCTYPE html>
{% load static %}
```  
add tags to html
```html
<img src="{% static "images/peppa.jpg" %}" alt="peppa pig">
```
can also add css file   
```html
<link rel="stylesheet" href="{% static "css/my_css.css" %}">
```
# model
go to the models.py under the app dir   
import the models class   
```py
from django.db import models
```
create models(tables)   
```py
class Topic(models.Model):
    top_name = models.CharField(max_length=264, unique=True)

    def __str__(self):
        return self.top_name

class Webpage(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    name = models.CharField(max_length=264, unique=True)
    url = models.URLField(unique=True)

    def __str__(self):
        return self.name

class AccessRecord(models.Model):
    name = models.ForeignKey(Webpage, on_delete=models.CASCADE)
    date = models.DateField()

    def __str__(self):
        return str(self.date)
```
## migrate
under the project dir   
```shell
python manage.py migrate
```
then migrate the app   
```shell
python manage.py makemigrations first_app
```
do the migrate again
```shell
python manage.py migrate
```
## use shell to add records to models
open interactive console   
```shell
python manage.py shell
```
```py
from first_app.models import Topic
```
```py
print(Topic.objects.all())
```
```py
t = Topic(top_name='Social Network')
```
```py
t.save()
```
```py
print(Topic.objects.all())
```
## use admin interface to manage records
go to the admin.py under the app dir   
import models from the app's models
```py
from first_app.models import Topic, Webpage, AccessRecord
```
register the models
```py
admin.site.register(Topic)
admin.site.register(Webpage)
admin.site.register(AccessRecord)
```
### create a super user
under the project dir
```shell
python manage.py createsuperuser
```
then follow the steps   
run the server and go to admin page, log in and play   
## populate with fake data
```shell
pip install Faker
```
create a populate_first_app.py under the top project dir   
```py
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'first_project.settings')

import django
django.setup()

import random
from first_app.models import Topic, Webpage, AccessRecord
from faker import Faker

fakegen = Faker()
topics = ['Search', 'Social', 'Marketplace', 'News', 'Games']

def add_topic():
    t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    return t

def populate(N=5):
    for entry in range(N):

        top = add_topic()

        fake_url = fakegen.url()
        fake_date = fakegen.date()
        fake_name = fakegen.company()

        wp = Webpage.objects.get_or_create(topic=top, url=fake_url, name=fake_name)[0]

        acc_rec = AccessRecord.objects.get_or_create(name=wp, date=fake_date)[0]

if __name__ == '__main__':
    print('populating script!')
    populate(20)
    print('populating complete')
```
run the file
