from django.shortcuts import render,redirect
from django.views.generic import (TemplateView, CreateView,FormView,RedirectView, ListView, UpdateView, DeleteView,
View, DetailView)
from django.contrib.auth.views import PasswordChangeView
from django.core.mail import send_mail
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from .forms import RegistrationForm, AdminCreateForm
from .models import MyUser, Institution, Gift


class LandingPage(TemplateView):
    template_name = 'index.html'


class ContactView(RedirectView):

    url = reverse_lazy('home')

    def post(self, request):
        
        send_mail(
            f"{request.POST.get('name')}, {request.POST.get('surname')}",
            f"Wiadomość od {request.POST.get('name')}: {request.POST.get('message')}",
            "",
            [''],
            fail_silently=False,)

        return self.get(request)


class AboutView(TemplateView):
    template_name = 'about.html'


class HowItWorksView(TemplateView):
    template_name = 'how_it_works.html'


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
        return reverse_lazy('home')


class LogoutView(LoginRequiredMixin ,RedirectView):
    login_url = reverse_lazy('login')
    url = reverse_lazy('home')

    def get(self, request, *args, **kwargs):
        logout(request)
        return super(LogoutView, self).get(request, *args, **kwargs)


class AdminListView(UserPassesTestMixin,ListView):
    login_url=reverse_lazy('login')
    queryset = MyUser.objects.filter(is_superuser=True)
    template_name = 'admin_list.html'

    def test_func(self):
        return self.request.user.is_superuser


class AdminEditView(UserPassesTestMixin,UpdateView):
    login_url=reverse_lazy('login')
    model = MyUser
    template_name = 'admin_edit.html'
    fields = ['first_name', 'last_name', 'email', 'username', 'is_active', 'is_staff']
    success_url = reverse_lazy('admin_list')

    def test_func(self):
        return self.request.user.is_superuser

class AdminCreateView(UserPassesTestMixin,CreateView):
    login_url=reverse_lazy('login')
    model = MyUser
    form_class = AdminCreateForm
    template_name = 'admin_create.html'
    success_url = reverse_lazy('admin_list')
    
    def get_initial(self):
        initial = super().get_initial()
        initial['is_superuser'] = True
        return initial

    def test_func(self):
        return self.request.user.is_superuser


class AdminDeleteView(UserPassesTestMixin,DeleteView):
    login_url = reverse_lazy('login')
    model = MyUser
    template_name = 'admin_delete.html'
    success_url = reverse_lazy('admin_list')

    def test_func(self):
        return self.request.user.is_superuser


class UserDetailsView(LoginRequiredMixin,DetailView):
    login_url = reverse_lazy('login')
    model = MyUser
    template_name = 'user_details.html'


class UserUpdateView(LoginRequiredMixin,UpdateView):
    model = MyUser
    template_name = 'user_edit.html'
    fields = ['first_name', 'last_name', 'email', 'username']

    def get_success_url(self):
        return reverse_lazy('user_details', kwargs={'pk':self.request.user.pk})


class UserChangePassword(LoginRequiredMixin,PasswordChangeView):
    success_url = reverse_lazy('home')
    template_name = 'user_password.html'


class AdminInstitutionList(UserPassesTestMixin,ListView):
    login_url=reverse_lazy('login')
    model = Institution
    template_name = 'admin_institutions.html'

    def test_func(self):
        return self.request.user.is_superuser


class AdminInstitutionCreate(UserPassesTestMixin,CreateView):
    login_url=reverse_lazy('login')
    model = Institution
    fields = '__all__'
    template_name = 'institution_create.html'
    success_url = reverse_lazy('admin_institutions')

    def test_func(self):
        return self.request.user.is_superuser

class InstitutionEditView(UserPassesTestMixin,UpdateView):
    login_url=reverse_lazy('login')
    model = Institution
    template_name = 'institution_edit.html'
    fields = '__all__'
    success_url = reverse_lazy('admin_institutions')

    def test_func(self):
        return self.request.user.is_superuser

class InstitutionDeleteView(UserPassesTestMixin,DeleteView):
    login_url=reverse_lazy('login')
    model = Institution
    template_name = 'institution_delete.html'
    success_url = reverse_lazy('admin_institutions')

    def test_func(self):
        return self.request.user.is_superuser


class UserInstitutionList(LoginRequiredMixin,AdminInstitutionList):
    template_name = 'user_institutions.html'


class GiftSentView(LoginRequiredMixin,View):
    login_url = reverse_lazy('login')
    def get(self,request):
        return render(request,'form.html')


    def post(self,request):
        gift = Gift.objects.create(type_of_thing=request.POST.get('products[]'),
                                    capacity=request.POST.get('bags'),
                                    localization=request.POST.get('localization'),
                                    for_who=request.POST.get('help[]'),
                                    street=request.POST.get('address'),
                                    city=request.POST.get('city'),
                                    post_code=request.POST.get('postcode'),
                                    phone_number=request.POST.get('phone'),
                                    date=request.POST.get('data'),
                                    time=request.POST.get('time'),
                                    info=request.POST.get('more_info'),
                                    user=MyUser.objects.get(pk=request.user.pk))

        return redirect(reverse_lazy('gift_sent'))