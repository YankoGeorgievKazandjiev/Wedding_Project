from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User



class LoginForm(ModelForm):
    class Meta:
        model = User
        fields = ['email', 'password']
        widgets = {
            'email':forms.TextInput(attrs={'placeholder':'E-mail:'}),
            'password': forms.PasswordInput(attrs={'placeholder':'Password:'})
        }


class RegisterForm(ModelForm):
    class Meta:
        model = User
        fields = ['email', 'password', 'first_name', 'last_name']
        widgets = {
            'password': forms.PasswordInput()
        }
