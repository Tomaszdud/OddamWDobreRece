from django.shortcuts import render,redirect
from django.views.generic import TemplateView, CreateView,FormView,RedirectView, ListView, UpdateView, DeleteView
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from .forms import RegistrationForm, AdminCreateForm
from .models import MyUser, Institution


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


class AdminListView(ListView):
    queryset = MyUser.objects.filter(is_superuser=True)
    template_name = 'admin_list.html'


class AdminEditView(UpdateView):
    model = MyUser
    template_name = 'admin_edit.html'
    fields = ['first_name', 'last_name', 'email', 'username', 'is_active', 'is_staff']
    success_url = reverse_lazy('admin_list')


class AdminCreateView(CreateView):
    model = MyUser
    form_class = AdminCreateForm
    template_name = 'admin_create.html'
    success_url = reverse_lazy('admin_list')
    
    def get_initial(self):
        initial = super().get_initial()
        initial['is_superuser'] = True
        return initial


class AdminDeleteView(DeleteView):
    model = MyUser
    template_name = 'admin_delete.html'
    success_url = reverse_lazy('admin_list')


class UserUpdateView(UpdateView):
    model = MyUser
    template_name = 'user_edit.html'
    fields = ['first_name', 'last_name', 'email', 'username']
    success_url = reverse_lazy('main_user')


class UserChangePassword(PasswordChangeView):
    success_url = reverse_lazy('main_user')
    template_name = 'user_password.html'


class AdminInstitutionList(ListView):
    model = Institution
    template_name = 'admin_institutions.html'


class AdminInstitutionCreate(CreateView):
    model = Institution
    fields = '__all__'
    template_name = 'institution_create.html'
    success_url = reverse_lazy('admin_institutions')


class InstitutionEditView(UpdateView):
    model = Institution
    template_name = 'institution_edit.html'
    fields = '__all__'
    success_url = reverse_lazy('admin_institutions')


class InstitutionDeleteView(DeleteView):
    model = Institution
    template_name = 'institution_delete.html'
    success_url = reverse_lazy('admin_institutions')
