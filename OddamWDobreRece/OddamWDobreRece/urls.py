"""OddamWDobreRece URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Oddam.views import (LandingPage,Registration,Login, LogoutView, AdminListView,\
     AdminEditView, AdminCreateView, AdminDeleteView, UserUpdateView, UserChangePassword, AdminInstitutionList,\
         AdminInstitutionCreate,InstitutionEditView, InstitutionDeleteView, UserInstitutionList,\
             GiftSentView,ContactView, AboutView,HowItWorksView,UserDetailsView, MyGiftView,\
                 MyGiftDetailsView,MyGiftUpdateView,)

             
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', LandingPage.as_view(),name='home'),
    path('about/',AboutView.as_view(), name='about'),
    path('howitworks/', HowItWorksView.as_view(), name='how_it_works'),
    path('registration/', Registration.as_view(), name='registration'),
    path('login/', Login.as_view(), name='login'),
    path('logout/', LogoutView.as_view(),name='logout'),
    path('admin/list/', AdminListView.as_view(), name='admin_list'),
    path('admin/edit/<int:pk>/', AdminEditView.as_view(), name='admin_edit'),
    path('admin/create/', AdminCreateView.as_view(), name = 'admin_create'),
    path('admin/delete/<int:pk>/', AdminDeleteView.as_view(), name = 'admin_delete'),
    path('user/edit/<int:pk>/', UserUpdateView.as_view(), name = 'user_edit'),
    path('user/change/password/', UserChangePassword.as_view(), name='user_password'),
    path('user/details/<int:pk>', UserDetailsView.as_view(), name='user_details'),
    path('admin/institution/list/', AdminInstitutionList.as_view(), name='admin_institutions'),
    path('admin/institution/create/', AdminInstitutionCreate.as_view(), name= 'institution_create'),
    path('institution/edit/<int:pk>/', InstitutionEditView.as_view(), name= 'institution_edit'),
    path('institution/delete/<int:pk>/', InstitutionDeleteView.as_view(), name= 'institution_delete'),
    path('redirect/contact/', ContactView.as_view(), name='contact'),
    path('user/institution/list/', UserInstitutionList.as_view(), name= 'user_institutions'),
    path('gift/sent/', GiftSentView.as_view(), name='gift_sent'),
    path('my/gift/', MyGiftView.as_view(), name='my_gift'),
    path('my/gift/details/<int:pk>', MyGiftDetailsView.as_view(), name='my_gift_details'),
    path('my/gift/taken/<int:pk>',MyGiftUpdateView.as_view(), name='my_gift_taken'),
]