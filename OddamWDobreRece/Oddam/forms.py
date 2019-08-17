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


class AdminCreateForm(UserCreationForm):
    class Meta:
        model = MyUser
        fields = ['username', 'first_name', 'last_name', 'email', 'is_staff','is_superuser', 'password1', 'password2']
        widgets = {'is_superuser':forms.HiddenInput()}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].widget = forms.TextInput(attrs={'placeholder': 'Email',
                                                            'name':'email'})
        self.fields['password1'].widget = forms.PasswordInput(attrs={'placeholder': 'Hasło',
                                                                    'name':'password1'})
        self.fields['password2'].widget = forms.PasswordInput(attrs={'placeholder': 'Powtórz Hasło',
                                                                    'name':'password2'})
        self.fields['username'].widget = forms.TextInput(attrs={'placeholder': 'Nazwa Użytkownika',
                                                            'name':'username'})
        self.fields['first_name'].widget = forms.TextInput(attrs={'placeholder': 'Imię',
                                                            'name':'first_name'})
        self.fields['last_name'].widget = forms.TextInput(attrs={'placeholder': 'Nazwisko',
                                                            'name':'last_name'})
                                                            