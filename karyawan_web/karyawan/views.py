from django.shortcuts import render, redirect
from .form import Step1Form, Step2Form
from karyawan.services.generate_id import generated_id
# Create your views here.


def tambah1(request):
    if request.method == 'POST':
        form = Step1Form(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            cleaned_data['tanggal_lahir'] = cleaned_data['tanggal_lahir'].isoformat()
            tahun_lahir = tanggal_lahir.year

            id = generated_id(tahun_lahir)

            request.session['step1'] = cleaned_data
            return redirect('tambah2')
    form = Step1Form()
    return render(request, 'tambah1.html', {'form': form})


def tambah2(request):
    data1 = request.session.get('step1')
    form = Step2Form(request.POST)
    if not data1:
        return redirect('step1')
    if data1:
        return render(request, 'tambah2.html', {'data1': data1}, {'form': form}, {'id': id})
