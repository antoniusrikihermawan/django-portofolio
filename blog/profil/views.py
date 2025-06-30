from django.shortcuts import render
from .forms import FormBarang

def portofolio(request):
    return render(request, 'index.html')

def form_barang(request):
    from_barang = FormBarang()
    return render(request, 'tambah.html', {'form_barang': from_barang})
   