from django.db import models

# Create your models here.
class Barang(models.Model):
    kodebarang = models.CharField(max_length=8)
    nama = models.CharField(max_length=50)
    stok = models.IntegerField()
    harga = models.BigIntegerField()
    link_gambar = models.CharField(max_length=150, blank=True)

    def __str__(self):
        return self.nama
