from django.conf import settings
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('portofolio/', views.portofolio),
    path('tambah/', views.form_barang, name='tambah'),
]