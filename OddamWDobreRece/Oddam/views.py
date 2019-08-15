from django.shortcuts import render,redirect
from django.views.generic import TemplateView, CreateView,FormView,RedirectView
from django.contrib.auth.models import User
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegistrationForm


class LandingPage(TemplateView):
    template_name = 'index.html'


class MainUser(LoginRequiredMixin,TemplateView):
    login_url = reverse_lazy('login')
    template_name = 'main_page_user.html'


class MainAdmin(TemplateView):
    template_name = 'main_page_admin.html'


class Registration(CreateView):
    template_name = 'register.html'
    form_class = RegistrationForm
    success_url = reverse_lazy('login')

    def form_valid(self,form):
        form.save()
        return super(Registration,self).form_valid(form)

class Login(FormView):
    template_name = 'login.html'
    form_class = AuthenticationForm

    def form_valid(self, form):
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')

        user = authenticate(username=username, password=password)
        login(self.request, user)
        return super().form_valid(form) 

    def get_success_url(self):
        if self.request.user.is_superuser:
            return reverse('main_admin')
        else:
            return reverse('main_user')


class LogoutView(RedirectView):
    url = reverse_lazy('home')

    def get(self, request, *args, **kwargs):
        logout(request)
        return super(LogoutView, self).get(request, *args, **kwargs)