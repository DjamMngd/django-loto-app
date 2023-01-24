"""loto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from tirages import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index, name="index"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
    path('email_sent/', views.email_sent, name="email_sent"),
    path('generate_loto_numbers/', views.generate_loto_numbers, name="generate_loto_numbers"),
    path('generate_euroMillion_numbers/', views.generate_euroMillion_numbers, name="generate_euroMillion_numbers"),
    path('newRandomLotoNumbers/', views.newRandomLotoNumbers, name="generate_NewRandomLotoNumbers"),
    path('newRandomEuroMillionNumbers/', views.newRandomEuroMillionNumbers, name="generate_NewRandomEuroMillionNumbers"),
]
