from django.shortcuts import render, redirect
from .form import Step1Form, Step2Form
import datetime
from karyawan.models import Karyawan


def tambah1(request):
    if request.method == 'POST':
        form = Step1Form(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            # Simpan tanggal lahir sebagai string ISO
            cleaned_data['tanggal_lahir'] = cleaned_data['tanggal_lahir'].isoformat()
            request.session['step1'] = cleaned_data
            return redirect('tambah2')
    else:
        form = Step1Form()
    return render(request, 'tambah1.html', {'form': form})


def tambah2(request):
    data1 = request.session.get('step1')
    if not data1:
        return redirect('tambah1')  # kalau belum isi step1

    # Ambil tahun lahir dari session
    tanggal_lahir = datetime.date.fromisoformat(data1['tanggal_lahir'])
    tahun_lahir = tanggal_lahir.year
    tahun_masuk = datetime.datetime.now().year

    prefix = f"{tahun_masuk}{tahun_lahir}"
    id_list = list(
        Karyawan.objects.filter(id__startswith=prefix).values_list('id', flat=True)
    )

    urutan_list = [int(id_str[-3:]) for id_str in id_list if id_str[-3:].isdigit()]
    urutan = max(urutan_list) + 1 if urutan_list else 1
    id_baru = f"{prefix}{urutan:03d}"

    # Siapkan form Step2
    if request.method == 'POST':
        form = Step2Form(request.POST)
        if form.is_valid():
            # simpan ke database di sini jika mau
            pass
    else:
        form = Step2Form()

    context = {
        'form': form,
        'data1': data1,
        'id': id_baru
    }

    return render(request, 'tambah2.html', context)
