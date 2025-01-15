"""
URL configuration for Command project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from django.shortcuts import render,redirect
from django.contrib.auth import views as auth_views
from django.contrib.auth import logout
from Home import views as app_views

def custom_logout(request):
    logout(request) 
    return redirect('logout_success')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include("Home.urls")),
    path('email/',include('Email.urls')),
    path('register',app_views.Register,name='Register'),
    path('login',auth_views.LoginView.as_view(template_name='Home/login.html'),name='login'),
    path('logout',custom_logout,name='logout'),
    path('logout-success',auth_views.TemplateView.as_view(template_name='Home/logout.html'), name='logout_success'),


]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
