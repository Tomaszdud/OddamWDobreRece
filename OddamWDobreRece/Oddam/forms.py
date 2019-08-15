from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django import forms
from .models import MyUser


class RegistrationForm(UserCreationForm):
    class Meta:
        model = MyUser
        fields = ['password1','password2','email']

    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        self.fields['email'].widget = forms.TextInput(attrs={'placeholder': 'Email',
                                                            'name':'email'})
        self.fields['password1'].widget = forms.PasswordInput(attrs={'placeholder': 'Hasło',
                                                                    'name':'password1'})
        self.fields['password2'].widget = forms.PasswordInput(attrs={'placeholder': 'Powtórz Hasło',
                                                                    'name':'password2'})
