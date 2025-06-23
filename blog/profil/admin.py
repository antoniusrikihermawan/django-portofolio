from django.contrib import admin
from . models import Barang, Jenis, About


# Register your models here.
class BarangAdmin(admin.ModelAdmin):
    list_display = ('kodebarang', 'nama', 'stok', 'harga', 'link_gambar', 'tgl_input', 'id_jenis')
    list_filter = ('kodebarang', 'nama', 'id_jenis__nama')
    list_per_page = 3
    search_fields = ('id_jenis__nama',)

admin.site.register(Barang, BarangAdmin)
admin.site.register(Jenis)
admin.site.register(About)

