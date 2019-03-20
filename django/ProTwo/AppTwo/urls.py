from django.urls import path, include, re_path
from AppTwo import views

urlpatterns = [
    re_path(r'^$', views.user_form_view, name='user_form'),
]
