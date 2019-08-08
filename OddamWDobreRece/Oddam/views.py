from django.shortcuts import render
from django.views.generic import TemplateView, CreateView
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .forms import RegistrationForm


class LandingPage(TemplateView):
    template_name = 'landing_page.html'


class Registration(CreateView):
    template_name = 'registration.html'
    form_class = RegistrationForm
    success_url = '/login'


