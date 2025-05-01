from django.db import models

# Create your models here.


class Karyawan(models.Model):
    id = models.CharField(max_length=11, unique=True, primary_key=True)
    nama = models.CharField(max_length=100)
    jabatan = models.CharField(max_length=20)
    lokasi = models.CharField(max_length=40)
