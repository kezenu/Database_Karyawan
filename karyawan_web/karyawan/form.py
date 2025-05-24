from django import forms


class step1(forms.Form):
    nama = forms.CharField(max_length=100, label='Nama Lengkap')
    tanggal_lahir = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), label='Tanggal Lahir (17-08-1945)')
    nik = forms.CharField(min_length=16, max_length=16, label='NIK KTP')
    no_hp = forms.CharField(max_length=13, min_length=10, label="Nomer Handphone")
    email = forms.EmailField(label='Email')
