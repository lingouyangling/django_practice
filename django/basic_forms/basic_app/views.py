from django.shortcuts import render
from basic_app import forms
# Create your views here.
def index(request):
    return render(request,'basic_app/index.html')

def name_form_view(request):
    form = forms.NameForm()

    if request.method =='POST':
        form = forms.NameForm(request.POST)
        if form.is_valid():
            print('validation success!'.upper())
            print('NAME: ' + form.cleaned_data['name'])
            print('EMAIL: ' + form.cleaned_data['email'])
            print('TEXT: ' + form.cleaned_data['text'])
    return render(request, 'basic_app/form_page.html', {'form': form})
