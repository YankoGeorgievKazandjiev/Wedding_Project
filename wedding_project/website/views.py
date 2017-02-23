from django.shortcuts import render
from django.views import View
from wedding_project.forms import RegisterForm, LoginForm
from django.views.generic import ListView, CreateView
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, HttpResponse, reverse
from django.views.generic.edit import FormView
from .forms import LoginForm

# Create your views here.


# def index(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         import ipdb; ipdb.set_trace()
#         user = authenticate(username=username, password=password)
#         if user is not None:
#             login(request, user)
#             return redirect(reverse('website:registerView'))
#         else:
#             return render(request, 'help.html', locals())

#     # form = LoginForm()
#     return render(request, 'main.html', locals())

class indexView(View):
    form_class = LoginForm
    template_name = 'main_html'

    def get(self, request):
        form = self.form_class(None)
        return render(self.request, 'main.html', {'form': form})


    def post(self, request):
        username = self.request.POST.get('username')
        password = self.request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(reverse('website:registerView'))
        else:
            return render(self.request, 'help.html', locals())
        form = self.form_class(self.request.POST)
        return redirect(reverse('website:registerView'))


def help(request):
    return render(request, 'help.html', locals())


class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = 'registration.html'

    def get(self, request):
        form = self.form_class(None)
        return render(self.request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(self.request.POST)
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
