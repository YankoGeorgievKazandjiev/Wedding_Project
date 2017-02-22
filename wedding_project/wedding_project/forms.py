from django import forms
from User.models import User


class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email', 'password','first_name', 'last_name']
        labels = {}
        widgets = {
    'password': forms.PasswordInput()
        }
    # first_name = forms.CharField()
    # last_name = forms.CharField()
    # email = forms.EmailField()
    # password = forms.CharField(widget=forms.PasswordInput())


class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())
