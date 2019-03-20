create a forms.py under the app dir
```py
from django import forms

class NameForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    text = forms.CharField(widget=forms.Textarea)

```
go to views.py
```py
from basic_app import forms

def name_form_view(request):
    # the first request is a GET, now only present a new form to the user
    form = forms.NameForm()

    # when user submit the form, the method is post
    if request.method =='POST':
        form = forms.NameForm(request.POST)
        if form.is_valid():
            print('validation success!'.upper())
            print('NAME: ' + form.cleaned_data['name'])
            print('EMAIL: ' + form.cleaned_data['email'])
            print('TEXT: ' + form.cleaned_data['text'])
    return render(request, 'basic_app/form_page.html', {'form': form})
```
go to the template file
```html
<form method="post">
    {{ form.as_p }}
    {% csrf_token %}
    <input type="submit" class="btn btn-primary" value="Submit">
</form>
```
add a bot catcher (not necessary) to the forms.py
```py
from django import forms

class NameForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    text = forms.CharField(widget=forms.Textarea)
    botcatcher = forms.CharField(required=False, widget=forms.HiddenInput)

    def clean_botcatcher(self):
        botcatcher = self.cleaned_date['botcatcher']
        if len(botcatcher) > 0:
            raise forms.ValidationError('GOTCHA BOT!')
        return botcatcher
```
## form validation
catch bots   
```py
from django import forms
from django.core import validators

class NameForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    text = forms.CharField(widget=forms.Textarea)
    botcatcher = forms.CharField(required=False,
                                widget=forms.HiddenInput,
                                validators=[validators.MaxLengthValidator(0)])

    # def clean_botcatcher(self):
    #     botcatcher = self.cleaned_date['botcatcher']
    #     if len(botcatcher) > 0:
    #         raise forms.ValidationError('GOTCHA BOT!')
    #     return botcatcher
```
customized validator
```py
from django import forms
from django.core import validators

def check_for_z(value):
    if value[0].lower() != 'z':
        raise forms.ValidationError('NAME NEEDS TO START WITH Z')


class NameForm(forms.Form):
    name = forms.CharField(validators=[check_for_z])
    email = forms.EmailField()
    text = forms.CharField(widget=forms.Textarea)
    botcatcher = forms.CharField(required=False,
                                widget=forms.HiddenInput,
                                validators=[validators.MaxLengthValidator(0)])
```
validate email   
```py
from django import forms
from django.core import validators

class NameForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    verify_email = forms.EmailField(label='Enter your email again:')
    text = forms.CharField(widget=forms.Textarea)

    def clean(self):
        all_clean_data = super().clean()
        email = all_clean_data['email']
        vmail = all_clean_data['verify_email']

        if email != vmail:
            raise forms.ValidationError('MAKE SURE EMAIL MATCH!')
```
