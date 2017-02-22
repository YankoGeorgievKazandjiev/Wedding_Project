from django.shortcuts import render
from django.views import View
from wedding_project.forms import RegisterForm, LoginForm
from django.views.generic import ListView
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, HttpResponse
from .forms import LoginForm

# Create your views here.


def index(request):
    # if request.method == 'post':
    #     username = request.POST['email']
    #     password = request.POST['password']
    #     user = authenticate(request, username=username, password=password)
    #     if user is not None:
    #         login(request, user)
    #         return render(request, 'help.html', locals())
    #     else:
    #         return HttpResponse("Invalid")
    form = LoginForm()
    return render(request, 'main.html', {'form': form})


def help(request):
    return render(request, 'help.html', locals())


class RegisterView(View):
    form_class = RegisterForm
    template_name = 'registration.html'

    def get(self, request):
        form = self.form_class(None)

        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():

            user = form.save(commit=False)
            first_name = form.cleaned_data['firts_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            user.save()


class LoginView(View):
    form_class = LoginForm
    template_name = 'login.html'

    def get(self, request):
        pass

    def post(self, request):
        pass


class GuestListView(ListView):
    pass
