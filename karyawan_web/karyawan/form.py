from django import forms
from .models import Karyawan


class Step1Form(forms.ModelForm):
    class Meta:
        model = Karyawan
        fields = ['nama', 'tanggal_lahir', 'nik', 'no_hp', 'email']
        widgets = {
            'tanggal_lahir': forms.DateInput(attrs={'type': 'date'})
        }


class Step2Form(forms.ModelForm):
    class Meta:
        model = Karyawan
        fields = ['jabatan', 'pendidikan', 'lokasi', 'kelamin']
