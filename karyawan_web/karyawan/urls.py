from django.urls import path
from . import views

urlpatterns = [
    path("tambah/", views.tambah_karyawan, name="tambah_karyawan.html"),
    path("karyawan/", views.daftar_karyawan, name="karyawan.html"),
]
