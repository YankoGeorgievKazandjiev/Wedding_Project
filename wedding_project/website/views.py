from django.shortcuts import render
from django.views import View
from wedding_project.forms import RegisterForm, LoginForm
from django.views.generic import ListView, CreateView, TemplateView, UpdateView
from django.contrib.auth.models import User
# from User.models import User
from django.contrib.auth import authenticate, login
from django.core.urlresolvers import reverse
from django.shortcuts import redirect, HttpResponse
# from django.views.generic.edit import FormView
from .forms import LoginForm , PresentForm , RegisterForm
from django.contrib.auth.mixins import LoginRequiredMixin
from User.models import Present


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


    def post(self, request):
        form = self.form_class(self.request.POST)
        if form.is_valid():
            user = User.objects.create_user(first_name=form.cleaned_data['first_name'],
            last_name=form.cleaned_data['last_name'],
            password=form.cleaned_data['password'],
            user_name=form.cleaned_data['email'])

            user.save()
            return redirect(reverse('website:index'))
        return HttpResponse("form's not valid")

class PresentListView(ListView):
    login_url = '/'
    redirect_field_name = 'present_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['gifts'] = Present.objects.filter(approved=False)
        return context

    def get_queryset(self):
        return Present.objects.all()


class PresentCreateView(CreateView):
    model = Present
    fields = ['present_name']
    template_name = "present_form.html"

    def form_valid(self, form):
        author = self.request.user
        present = form.save(commit=False)
        # import ipdb; ipdb.set_trace()
        present.present_name = self.request.POST.get('text')
        present.reserved_by = author
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('website:present')


class ReserveView(UpdateView):
    model = Present
    fields = ['approved']

    def get_success_url(self):
        return reverse('website:present')




            # present.save()
            # present_name = forms.save(commit=True)
    # reserved_by = forms.save()
    # user = form.save(commit=False)
    # first_name = form.cleaned_data['first_name']
    # last_name = form.cleaned_data['last_name']
    # email = form.cleaned_data['email']
    # password = form.cleaned_data['password']
    # is_superuser = 1
