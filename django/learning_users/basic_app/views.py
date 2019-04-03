from django.shortcuts import render

from basic_app.models import UserProfileInfo
from basic_app.forms import UserForm, UserProfileForm

# Create your views here.
def index(request):
    return render(request, 'basic_app/index.html')

def register(request):
    registered = False
    if request == "POST":
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
