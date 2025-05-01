from django.shortcuts import render, redirect
from .form import KaryawanForm

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
