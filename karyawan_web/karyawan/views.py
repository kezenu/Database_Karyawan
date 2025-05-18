from django.shortcuts import render, redirect
from .form import KaryawanForm
from .models import Karyawan

# Create your views here.


def tambah_karyawan(request):
    if request.method == "POST":
        form = KaryawanForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
    else:
        form = KaryawanForm()
    return render(request, "tambah_karyawan.html", {"form": form})


def daftar_karyawan(request):
    semua_karyawan = Karyawan.objects.all()
    return render(request, 'karyawan.html', {'karyawan_list': semua_karyawan})
