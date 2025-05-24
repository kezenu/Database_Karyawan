from django.shortcuts import render, redirect
from .form import step1
# Create your views here.


def tambah1(request):
    if request.method == 'POST':
        form = step1(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            cleaned_data['tanggal_lahir'] = cleaned_data['tanggal_lahir'].isoformat()
            request.session['step1'] = cleaned_data
            return redirect('tambah2')
    form = step1()
    return render(request, 'tambah1.html', {'form': form})


def tambah2(request):
    data1 = request.session.get('step1')
    if not data1:
        return redirect('step1')
    if data1:
        return render(request, 'tambah2.html', {'data1': data1})
