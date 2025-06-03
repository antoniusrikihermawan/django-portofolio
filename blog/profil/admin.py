from django.contrib import admin
from . models import Barang

# Register your models here.
class BarangAdmin(admin.ModelAdmin):
    list_display = ('kodebarang', 'nama', 'stok', 'harga', 'link_gambar')
    list_filter = ('nama',)
    search_fields = ('nama', 'harga')

admin.site.register(Barang, BarangAdmin)

