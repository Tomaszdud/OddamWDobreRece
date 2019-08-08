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
from Oddam.views import LandingPage,Registration,Login, MainUser, MainAdmin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', LandingPage.as_view()),
    path('registration/', Registration.as_view()),
    path('login/', Login.as_view()),
    path('main/user', MainUser.as_view(), name='main_user'),
    path('main/admin', MainAdmin.as_view(), name='main_admin'),
]
