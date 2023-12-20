from django import forms


class UserSignForm(forms.Form):
    username = forms.CharField(widget= forms.TextInput(attrs= {'class': 'form-control', 'placeholder':'Enter your Username'}))
    email = forms.EmailField(widget= forms.EmailInput(attrs= {'class': 'form-control', 'placeholder':'Enter your Email'}))
    password = forms.CharField(widget= forms.PasswordInput(attrs= {'class': 'form-control', 'placeholder':'Enter your Password'}))
