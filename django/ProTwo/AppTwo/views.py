from django.shortcuts import render
# from django.http import HttpResponse
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
