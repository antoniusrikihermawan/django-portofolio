from django.forms import ModelForm
from . models import Barang
from django import forms

class FormBarang(ModelForm):
    class Meta:
        model = Barang
        fields = '__all__'
        widgets = {
            'Kodebarang': forms.TextInput(attrs={'class':'form-control'}),
            'Nama': forms.TextInput(attrs={'class':'form-control'}),
            'Stok': forms.NumberInput(attrs={'class':'form-control'}),
            'Harga': forms.NumberInput(attrs={'class':'form-control'}),
            'Link gambar': forms.TextInput(attrs={'class':'form-control'}),
            'Id jenis': forms.Select(attrs={'class':'form-control'}),
        }


