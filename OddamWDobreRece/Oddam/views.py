from django.shortcuts import render,redirect
from django.views.generic import TemplateView, CreateView,FormView,RedirectView
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate,login, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegistrationForm


class LandingPage(TemplateView):
    template_name = 'landing_page.html'


class MainUser(LoginRequiredMixin,TemplateView):
    login_url = '/login'
    template_name = 'main_page_user.html'


class MainAdmin(TemplateView):
    template_name = 'main_page_admin.html'


class Registration(CreateView):
    template_name = 'registration.html'
    form_class = RegistrationForm
    success_url = '/login'


class Login(FormView):
    template_name = 'login.html'
    form_class = AuthenticationForm

    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']

        user = authenticate(username=username, password=password)
        login(self.request, user)
        return super().form_valid(form)

    def get_success_url(self):
        if self.request.user.is_superuser:
            return reverse('main_admin')
        else:
            return reverse('main_user')


class LogoutView(RedirectView):
    url = '/'

    def get(self, request, *args, **kwargs):
        logout(request)
        return super(LogoutView, self).get(request, *args, **kwargs)