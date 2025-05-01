from django.shortcuts import render
from .models import hello


def hello_view(request):
    Halo = hello.objects.first()
    return render(request, 'karyawan/hello.html', {'Message': Halo.pesan})
