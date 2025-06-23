from django.conf import settings
# from django.conf.urls.static static
# from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('portofolio/', views.portofolio),   
]