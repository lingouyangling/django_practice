from django.urls import path, include, re_path
from first_app import views

urlpatterns =[
    re_path(r'^$', views.index, name='index'),
]
