from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
# from User.models import User



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
        fields = ['first_name', 'last_name','email', 'password']
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder':'First name:'}),
            'last_name': forms.TextInput(attrs={'placeholder':'Last name:'}),
            'email': forms.TextInput(attrs={'placeholder':'E-mail:'}),
            'password': forms.PasswordInput(attrs={'placeholder':'Password:'})
        }
