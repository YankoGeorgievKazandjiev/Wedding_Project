from django.shortcuts import render
from django.views import View
from wedding_project.forms import RegisterForm, LoginForm
from django.views.generic import ListView, CreateView, TemplateView
from django.contrib.auth.models import User
# from User.models import User
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, HttpResponse, reverse
# from django.views.generic.edit import FormView
from .forms import LoginForm
from django.contrib.auth.mixins import LoginRequiredMixin
from User.models import Present


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
        username = self.request.POST.get('email')
        password = self.request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            if user.is_superuser:
                return redirect(reverse('website:AdminView'))
            else:
                return redirect(reverse('website:present'))
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
            user = User.objects.create_user(first_name=form.cleaned_data['first_name'],
            last_name=form.cleaned_data['last_name'],
            password=form.cleaned_data['password'],
            email=form.cleaned_data['email'],
            username=form.cleaned_data['email'],
            is_superuser=0)

            # user = form.save(commit=False)
            # first_name = form.cleaned_data['first_name']
            # last_name = form.cleaned_data['last_name']
            # email = form.cleaned_data['email']
            # password = form.cleaned_data['password']
            # is_superuser = 1

            user.save()
            return redirect(reverse('website:index'))
        return HttpResponse("form's not valid")


class AdminView(TemplateView):
    # login_url = '/'
    # redirect_field_name = 'admin_page.html'
    template_name = "admin_page.html"
    def get_queryset(self):
        return redirect(redirect_field_name)

    # def get_queryset(self):
    #     return User.objects.all()
    # form_class = LoginForm
    # template_name = 'login.html'
    #
    def get(self, request,*args, **kwargs):
        return super().get(self, *args, **kwargs)
    #
    # def post(self, request):
    #     pass


class GuestListView(LoginRequiredMixin, ListView):

    login_url = '/'
    redirect_field_name = 'present_list.html'

    def get_queryset(self):
        return User.objects.all()
        # return redirect(reverse('website:guests'))


class PresentListView(ListView):
    
    def get_queryset(self):
        return Present.objects.all()
