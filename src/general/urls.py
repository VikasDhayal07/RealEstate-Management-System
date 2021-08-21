"""realestate URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from general import views

urlpatterns = [
    path("", views.index, name='home'),
    path("index/", views.index, name='index'),
    path("agent/", views.agent, name='agent'),
    path("search/", views.search, name='search'),
    path("owner/", views.owner, name='owner'),
    path("admin/", views.admin, name='admin'),
    path("regis/", views.regis, name='regis'),
    path("loga/", views.loga, name='login_agent'),
    path("logb/", views.logb, name='login_buyer'),
    path("logo/", views.logo, name='login_owner'),
]
