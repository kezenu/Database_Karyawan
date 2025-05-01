from django.urls import path
from . import views

urlpatterns = [
    path("tambah/", views.tambah_karyawan, name="tambah_karyawan.html"),
]
